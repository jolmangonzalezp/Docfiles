<?php

use App\Http\Controllers\NoteController;
use Illuminate\Support\Facades\Route;

Route::prefix('/v1')->resource('/note', NoteController::class);
