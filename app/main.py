from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List
from uuid import uuid4

app = FastAPI(title="Notes Microservice")

class NoteIn(BaseModel):
    title: str
    content: str

class Note(NoteIn):
    id: str

# Almacenamiento en memoria (demo)
_db: Dict[str, Note] = {}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/notes/", response_model=Note, status_code=201)
def create_note(note_in: NoteIn):
    nid = str(uuid4())
    # pydantic v2: use model_dump()
    note = Note(id=nid, **note_in.model_dump())
    _db[nid] = note
    return note

@app.get("/notes/", response_model=List[Note])
def list_notes():
    return list(_db.values())

@app.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: str):
    note = _db.get(note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@app.put("/notes/{note_id}", response_model=Note)
def update_note(note_id: str, note_in: NoteIn):
    note = _db.get(note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    updated = Note(id=note_id, **note_in.model_dump())
    _db[note_id] = updated
    return updated

@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: str):
    if note_id not in _db:
        raise HTTPException(status_code=404, detail="Note not found")
    del _db[note_id]
    return None