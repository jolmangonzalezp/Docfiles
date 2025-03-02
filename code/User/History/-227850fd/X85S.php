<?php

namespace App\Http\Controllers;

use App\Models\Note;
use Illuminate\Http\Request;
use App\Http\Requests\NoteRequest;
use Illuminate\Http\JsonResponse;
use App\Http\Resources\NoteResource;

class NoteController extends Controller
{
    public function index():JsonResponse
    {
        // $notes = Note::all();
        // return response()->json($notes, 200);
        return new NoteResource::collection(Note::all());
    }

    /**
     * Show the form for creating a new resource.
     */
    public function store(NoteRequest $request):JsonResponse
    {
        $note = Note::create($request->all());
        return response()->json(
            [
                'success' => true,
                'data' => $note
            ],
            201
        );
    }

    /**
     * Display the specified resource.
     */
    public function show(string $id):JsonResponse 
    {
        $note = Note::find($id);
        return response()->json($note, 200);
    }

    public function update(NoteRequest $request, string $id)
    {
        $note = Note::find($id);
        $note->update($request->all());
        return response()->json([
            'success' => true,
            'data' => $note
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
