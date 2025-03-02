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
<<<<<<< Tabnine <<<<<<<
        RateLimiter::for('api', function(Request $request){//-
        use Illuminate\Http\Request;//+
        use Illuminate\Support\Facades\RateLimiter;//+
        use Illuminate\Cache\RateLimiting\Limit;//+
//+
        RateLimiter::for('api', function (Request $request) {//+
            return Limit::perMinute(60)->by($request->user()?->id ?: $request->ip());
        });
>>>>>>> Tabnine >>>>>>>// {"conversationId":"e68e1c14-8fbf-4c7f-a084-176e97af5f1e","source":"instruct"}
    }

}
