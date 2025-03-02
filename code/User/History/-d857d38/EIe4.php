<?php

namespace App\Providers;

use Illuminate\Support\ServiceProvider;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\RateLimiter;
use App\Providers\Limit;

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
<<<<<<< Tabnine <<<<<<<
    protected function configureRateLimiter(): void//+
    {
        RateLimiter::for('api', function(Request $request){
            return Limit::perMinute(60)->by($request->user()?->id ?: $request->ip());
        });
    }
>>>>>>> Tabnine >>>>>>>// {"conversationId":"438ea36a-6540-4610-a693-3d41823a5624","source":"instruct"}

}
