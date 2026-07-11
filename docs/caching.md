# Redis Cache Documentation

## Implementation

This project currently configures Django cache using in-memory storage:

```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}
```

## What is Cached

- The project does not explicitly store custom cache keys.
- `categoriesApp` uses `cache_page` decorators on class-based views.

## Cache Lifetime

- Category list, category detail, and category products views are cached for 5 minutes.

## Cache Key Design

- DRF and Django generate cache keys automatically based on request path and user state.
- There is no custom cache key implementation.

## Cache Invalidation

- Invalidation is not explicitly implemented.
- Cache expires after 5 minutes by decorator settings.

## Performance Benefits

- `cache_page` reduces duplicate queries for category endpoints.
- Since data is read-heavy, this reduces response time for repeated category requests.

## Notes

- Redis is referenced in `.env` but not configured in Django settings.
- The current cache backend is local memory only.
