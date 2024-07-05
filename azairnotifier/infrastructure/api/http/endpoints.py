from fastapi import APIRouter, Depends, HTTPException
from dependency_injector.wiring import inject, Provide
from azairnotifier.application.handler.queryhandler import \
    GetFlightSearchesQueryHandler, \
    GetFlightSearchesByParametersQueryHandler
from azairnotifier.application.command import \
    CreateFlightSearchCommand, \
    DeleteFlightSearchCommand, \
    UpdateFlightSearchCommand
from azairnotifier.application.provider import AirportsProvider
from azairnotifier.application.handler.commandhandler import \
    CreateFlightSearchHandler, \
    DeleteFlightSearchHandler, \
    UpdateFlightSearchHandler
from azairnotifier.infrastructure.api.http.request import CreateFlightSearchRequest, UpdateFlightSearchRequest
from azairnotifier.config.di.container import Container

router = APIRouter()


@router.get('/airports')
@inject
async def get_airports(airports_provider: AirportsProvider = Depends(Provide[Container.airports_provider])) -> dict:
    return airports_provider.get_airports()

@router.get('/flight_searches')
@inject
async def get_flight_search(
        email: str = None,
        unsubscribe_code: str = None,
        get_flight_searches_query_handler: GetFlightSearchesByParametersQueryHandler = Depends(Provide[Container.get_flight_searches_by_parameters_query_handler])
) -> dict:
    try:
        assert email is not None or unsubscribe_code is not None
        flight_search = get_flight_searches_query_handler.get_by_email(email) \
            if email is not None \
            else get_flight_searches_query_handler.get_by_unsubscribe_code(unsubscribe_code)

        return flight_search.model_dump() if flight_search is not None else {}
    except AssertionError:
        raise HTTPException(status_code=400, detail="Invalid parameters: either email or unsubscribe_code should be passed")


@router.get('/flight_searches/{id}')
@inject
async def get_flight_search(
        id: str,
        get_flight_searches_query_handler: GetFlightSearchesQueryHandler = Depends(Provide[Container.get_flight_searches_query_handler])
) -> dict:
    try:
        flight_search = get_flight_searches_query_handler.get_by_pk(id)
        assert flight_search is not None

        return flight_search.model_dump()
    except AssertionError:
        raise HTTPException(status_code=404, detail="Flight search not found")

@router.post('/flight_searches', status_code=201)
@inject
async def add_flight(
        flight_search: CreateFlightSearchRequest,
        create_flight_search_handler: CreateFlightSearchHandler = Depends(
            Provide[Container.create_flight_search_handler]
        )
) -> dict:
    created_id = create_flight_search_handler.handle(CreateFlightSearchCommand.model_validate(flight_search.model_dump()))

    return {'id': created_id}


@router.put('/flight_searches/{id}')
@inject
async def update_flight(
        flight_search: UpdateFlightSearchRequest,
        id: str = None,
        update_flight_search_handler: UpdateFlightSearchHandler = Depends(
            Provide[Container.update_flight_search_handler]
        )
) -> dict:
    command = UpdateFlightSearchCommand.model_validate({'pk': id} | flight_search.model_dump())
    update_flight_search_handler.handle(command)

    return {'id': id}


@router.delete('/flight_searches', status_code=204)
@inject
async def delete_flight(
        code: str = None,
        delete_flight_search_handler: DeleteFlightSearchHandler = Depends(
            Provide[Container.delete_flight_search_handler]
        )
) -> None:
    if code is None:
        raise HTTPException(status_code=400, detail="Code is required")

    delete_flight_search_handler.handle(DeleteFlightSearchCommand(code=code))