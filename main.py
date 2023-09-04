import uvicorn
from fastapi import FastAPI, status, responses
from fastapi_chameleon import global_init  #type: ignore
from views import (
    home,
    courses,
    account,
)
from chameleon import PageTemplateFile      #type: ignore
from docopt import docopt
from fastapi.staticfiles import StaticFiles
from infrastructure.middleware import add_global_request_middleware
from database.database import delete_metadata
from services.auth_service import HTTPUnauthorizedAccess, HTTPUnauthorizedOnly
from infrastructure.viewmodel import ViewModel


TEMPLATES_DIR_PATH = './templates'
TEMPLATES_ERROR_PATH = f'{TEMPLATES_DIR_PATH}/errors'

app = FastAPI()

# for view in [home, courses, account]:
#     app.include_router(view.router)

# app.include_router(home.router)
# app.include_router(courses.router)
# app.include_router(account.router)


  
def main():
    config()
    start_server()
    
def config():
    print("[+] Configuring server")
    config_middleware()
    print('[+]...middleware configured')
    config_templates()
    print('[+] ... templates configured')
    config_exception_handlers()
    print('[+] ... templates configured')
    config_routes()
    print('[+... routes configured]')
    print("[+] done configuring server")

def config_middleware():
    add_global_request_middleware(app)
    
def config_routes():
    app.mount('/static', StaticFiles(directory='static'), name='static')
    for view in [home, courses, account]:
        app.include_router(view.router)
    
def config_templates():
    global_init(TEMPLATES_DIR_PATH)
    
def config_exception_handlers():
    async def unauthenticated_access_handler(*_, **__):
        template = PageTemplateFile(f'{TEMPLATES_ERROR_PATH}/404.pt')
        content = template(**ViewModel())
        return responses.HTMLResponse(content, status_code = status.HTTP_404_NOT_FOUND)
    
    async def unauthenticated_only_area_handler(*_, **__):
        return responses.RedirectResponse(url = '/', status_code = status.HTTP_302_FOUND)

    app.add_exception_handler(HTTPUnauthorizedAccess, unauthenticated_access_handler)
    app.add_exception_handler(status.HTTP_404_NOT_FOUND, unauthenticated_access_handler)
    app.add_exception_handler(HTTPUnauthorizedOnly, unauthenticated_only_area_handler)


def start_server():
    print("[+] Starting server")

    help_doc = """
A Web accessible FastAPI server that allow players to register/enroll for tournaments.

Usage:
    app.py [-d] [-p PORT] [-h HOST_IP] [-r]
    
Options:
    -p PORT, --port=PORT        Listen on this port [default: 8000]
    -r, --reload                Reload server when a file changes
    -h HOST_IP, --host=HOST_IP  Listen on this IP address [default: 127.0.0.1]
    -d, --delete-db             Delete existing database
"""

    args = docopt(help_doc)
    # create_ddl = args['--create-ddl']
    # populate_db = args['--populate-db']
    # rel = args['--reload']
    
    # if create_ddl:
    #     print("Will create ddl")
    #     if populate_db:
    #         print("Will also populate de DB")
    delete_db = args['--delete-db']
    if delete_db:
        delete_metadata()
            
    uvicorn.run('main:app',
                port = int(args['--port']),
                host = args['--host'],
                reload  = args['--reload'],
                reload_includes = ['*.pt'])

   
if __name__ == '__main__':
    main()
else:
    config()
    