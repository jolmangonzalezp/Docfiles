<?php

namespace App\Http\Controllers;

use App\Models\Note;
use Illuminate\Http\Request;
use App\Http\Requests\NoteRequest;

class NoteController extends Controller
{
    /**
     * Display a listing of the resource.
     */

    public function index()
    {
        $notes = Note::all();
        return response()->json($notes, 200);
    }

    /**
     * Show the form for creating a new resource.
     */
    public function store(NoteRequest $request)
    {
        $note = Note::create($request->all());
        return response()->json(
            [
                'success' => true
            ],
            201
        );
    }

    /**
     * Display the specified resource.
     */
    public function show(string $id)
    {
        $note = Note::find($id);
        return response()->json($note, 200);
    }

    public function update(NoteRequest $request, string $id)
    {
        $note = Note::find($id);
        $note->update($request->all());
        return response()->json([
            'success' => true
        ], 200);
    }

    public function destroy(string $id)
    {
        $note = Note::find($id);
        $note->delete();
        return response()->json([
            'success' => true
        ], 200);
    }
}
