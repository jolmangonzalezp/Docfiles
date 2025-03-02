<?php

namespace App\Providers;

use Illuminate\Support\ServiceProvider;
use Illuminate\Http\Request;
use App\Providers\RateLimiter;
use Illuminate\Support\Facades\RateLimiter as Limit;

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
        RateLimiter::for('api', function(Request $request){
            return Limit::perMinute(60)->by($request->user()?->id ?: $request->ip());
        });
    }

}
