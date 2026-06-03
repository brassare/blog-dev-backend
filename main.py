import uuid
from datetime import datetime, timezone
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 


app = FastAPI()

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

posts = [
    {
        "id": str(uuid.uuid4()),
        "title": "Comecando com React 19 e os novos hooks",
        "content": "React 19 trouxe uma serie de melhorias importantes para quem desenvolve interfaces modernas. Entre as principais novidades estao os hooks `use()`, `useOptimistic()` e o Server Components estavel. Neste post, vamos explorar como esses recursos mudam a forma de pensar componentes e como tirar proveito deles em projetos reais. O foco esta em entender quando usar cada um e quais armadilhas evitar. O mais bacana e que muita coisa que antes exigia bibliotecas externas agora vem de fabrica.",
        "flag": ["REACT", "HOOKS", "FRONTEND"],
        "created_at": datetime.now(timezone.utc).isoformat(),
    },
    {
        "id": str(uuid.uuid4()),
        "title": "FastAPI na pratica: construindo uma API em minutos",
        "content": "FastAPI virou uma das escolhas favoritas da comunidade Python para criar APIs rapidas, tipadas e com documentacao automatica. Neste guia montamos uma API REST completa, com autenticacao JWT, validacao via Pydantic e deploy em containers. O resultado e uma base solida que voce pode reutilizar em qualquer projeto.",
        "flag": ["PYTHON", "FASTAPI", "BACKEND"],
        "created_at": datetime.now(timezone.utc).isoformat(),
    },
    {
        "id": str(uuid.uuid4()),
        "title": "Como conseguir sua primeira vaga dev em 2026",
        "content": "O mercado dev mudou bastante nos ultimos anos. Hoje, mais do que dominar uma stack, recrutadores buscam pessoas que sabem comunicar, aprender rapido e entregar valor. Neste post compartilho 5 estrategias que vejo funcionando com alunos da mentoria: portfolio com projetos reais, contribuicao open source, networking ativo, presenca tecnica em redes sociais e processos seletivos bem preparados.",
        "flag": ["CAREIRA", "PRIMEIRO-EMPREGO", "MENTORIA"],
        "created_at": datetime.now(timezone.utc).isoformat(),
    },
    {
        "id": str(uuid.uuid4()),
        "title": "Git rebase vs merge: qual usar e quando",
        "content": "Uma das duvidas mais frequentes em times que adotam Git e quando fazer merge e quando fazer rebase. A verdade e que nao existe bala de prata: cada um resolve um problema diferente. Vamos passar por exemplos praticos, cenarios de conflito e a regra de ouro do rebase: nunca em branches publicas.",
        "flag": ["GIT", "WORKFLOW", "BOAS-PRATICAS"],
        "created_at": datetime.now(timezone.utc).isoformat(),
    },
    {
        "id": str(uuid.uuid4()),
        "title": "TypeScript: tipos utilitarios que voce precisa conhecer",
        "content": "Partial, Pick, Omit, Record, ReturnType... A biblioteca padrao de TypeScript e cheia de joias que economizam dezenas de linhas de codigo. Neste post organizamos os tipos utilitarios mais usados em produtos reais, com exemplos de quando aplicar e quais armadilhas evitar (sim, abusar de `any` ainda e a maior delas).",
        "flag": ["TYPESCRIPT", "TIPOS", "DX"],
        "created_at": datetime.now(timezone.utc).isoformat(),
    },
    {
        "id": str(uuid.uuid4()),
        "title": "Deploy na Vercel + Supabase em 10 minutos",
        "content": "Quer colocar seu projeto no ar sem dor de cabeca? Vercel + Supabase e uma combinacao excelente para projetos pessoais e MVPs. Neste passo a passo configuramos o projeto, conectamos ao banco Postgres do Supabase, ajustamos variaveis de ambiente e fazemos o primeiro deploy. Em 10 minutos voce tem URL publica funcionando.",
        "flag": ["DEPLOY", "VERCEL", "SUPABASE"],
        "created_at": datetime.now(timezone.utc).isoformat(),
    },
]

@app.get("/")
async def root():     
    return {"message": "Welcome"}

@app.get("/posts")
async def listar_posts():
    return posts