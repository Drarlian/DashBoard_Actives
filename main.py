from fastapi import FastAPI
from starlette.middleware.wsgi import WSGIMiddleware
# from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from functions.dash_board_functions.dash_functions import create_dash

# Criando a aplicação FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

dash_app = create_dash()

# Adicionando o Dash à aplicação FastAPI
app.mount("/dash", WSGIMiddleware(dash_app.server))


# @app.get("/")
# async def redirect_to_dash():
#     # Redirecionando a rota raiz para o dashboard
#     # return RedirectResponse(url="/dash")


# Rodando o servidor
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
