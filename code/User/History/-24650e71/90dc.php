<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;

class NoteRequest extends FormRequest
{
    /**
     * Determine if the user is authorized to make this request.
     */
    public function authorize(): bool
    {
        return true;
    }

    /**
     * Get the validation rules that apply to the request.
     *
     * @return array<string, \Illuminate\Contracts\Validation\ValidationRule|array<mixed>|string>
     */
    public function rules(): array
    {
        return [
            'title' => 'required|max:255|min:3',
            'content' => 'required|min:10|max:1000',
            'priority' => 'required|in:low,medium,high',
            'status' => 'required|in:active,inactive',
            'due_date' => 'required|date',
            'user_id' => 'required|exists:users,id'
        ];
    }
}
