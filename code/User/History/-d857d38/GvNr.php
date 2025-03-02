<?php

namespace App\Providers;

use Illuminate\Support\ServiceProvider;

class RouteServiceProvider extends ServiceProvider
{
    /**
     * Register services.
     */
    public function register(): void
    {

    }

    /**
     * Bootstrap services.
     */
    public function boot(): void
    {
        
    }

    protected function configureRateLimiter(): void
    {
        // $this->app['router']->middleware('throttle:60,1')->group(function () {
        //     // Define your route group with rate limiting here
        // });
    }

}
