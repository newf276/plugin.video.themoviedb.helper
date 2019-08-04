import sys
import xbmcplugin
import xbmcaddon

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])
# Get the add-on path
_addonpath = xbmcaddon.Addon().getAddonInfo('path')
# Get the api keys
_omdb_apikey = xbmcplugin.getSetting(_handle, 'omdb_apikey')
_tmdb_apikey = '?api_key=' + xbmcplugin.getSetting(_handle, 'tmdb_apikey')
# Get the language TODO: make user setting, not hardcoded
_language = '&language=en-US'
# Set http paths
OMDB_API = 'http://www.omdbapi.com/'
TMDB_API = 'https://api.themoviedb.org/3'
IMAGEPATH = 'https://image.tmdb.org/t/p/original/'

# Categories pass tmdb_id to path using .format(*args)
CATEGORIES = {'cast':
              {'types': ['movie', 'tv'],
               'name': 'Cast',
               'path': '{self.request_tmdb_type}/{self.request_tmdb_id}/credits',
               'key': 'cast',
               'list_type': '{self.request_tmdb_type}',
               'next_type': 'person',
               'next_info': 'details',
               },
              'crew':
              {'types': ['movie', 'tv'],
               'name': 'Crew',
               'path': '{self.request_tmdb_type}/{self.request_tmdb_id}/credits',
               'key': 'crew',
               'list_type': '{self.request_tmdb_type}',
               'next_type': 'person',
               'next_info': 'details',
               },
              'recommendations':
              {'types': ['movie', 'tv'],
               'name': 'Recommended',
               'path': '{self.request_tmdb_type}/{self.request_tmdb_id}/recommendations',
               'key': 'results',
               'list_type': '{self.request_tmdb_type}',
               'next_type': '{self.request_tmdb_type}',
               'next_info': 'details',
               },
              'similar':
              {'types': ['movie', 'tv'],
               'name': 'Similar',
               'path': '{self.request_tmdb_type}/{self.request_tmdb_id}/similar',
               'key': 'results',
               'list_type': '{self.request_tmdb_type}',
               'next_type': '{self.request_tmdb_type}',
               'next_info': 'details',
               },
              'keywords_movie':
              {'types': ['movie'],
               'name': 'Keywords',
               'path': '{self.request_tmdb_type}/{self.request_tmdb_id}/keywords',
               'key': 'keywords',
               'list_type': 'keyword',
               'next_type': '',
               'next_info': '',
               },
              'keywords_tv':
              {'types': ['tv'],
               'name': 'Keywords',
               'path': '{self.request_tmdb_type}/{self.request_tmdb_id}/keywords',
               'key': 'results',
               'list_type': 'keyword',
               'next_type': '',
               'next_info': '',
               },
              'search':
              {'types': ['movie', 'tv', 'person'],
               'name': 'Search {self.plural_type}',
               'path': 'search/{self.request_tmdb_type}',
               'key': 'results',
               'list_type': '{self.request_tmdb_type}',
               'next_type': '{self.request_tmdb_type}',
               'next_info': 'details',
               },
              'find':
              {'types': ['movie', 'tv'],
               'name': 'Find IMDb ID ({self.plural_type})',
               'path': 'find/{self.imdb_id}',
               'key': '{self.request_tmdb_type}_results',
               'reroute': 'details',
               },
              'popular':
              {'types': ['movie', 'tv', 'person'],
               'name': 'Popular {self.plural_type}',
               'path': '{self.request_tmdb_type}/popular',
               'key': 'results',
               'list_type': '{self.request_tmdb_type}',
               'next_type': '{self.request_tmdb_type}',
               'next_info': 'details',
               },
              'top_rated':
              {'types': ['movie', 'tv'],
               'name': 'Top Rated {self.plural_type}',
               'path': '{self.request_tmdb_type}/top_rated',
               'key': 'results',
               'list_type': '{self.request_tmdb_type}',
               'next_type': '{self.request_tmdb_type}',
               'next_info': 'details',
               },
              'upcoming':
              {'types': ['movie'],
               'name': 'Upcoming {self.plural_type}',
               'path': '{self.request_tmdb_type}/upcoming',
               'key': 'results',
               'list_type': '{self.request_tmdb_type}',
               'next_type': '{self.request_tmdb_type}',
               'next_info': 'details',
               },
              'airing_today':
              {'types': ['tv'],
               'name': 'Airing Today',
               'path': '{self.request_tmdb_type}/airing_today',
               'key': 'results',
               'list_type': '{self.request_tmdb_type}',
               'next_type': '{self.request_tmdb_type}',
               'next_info': 'details',
               },
              'now_playing':
              {'types': ['movie'],
               'name': 'In Theatres',
               'path': '{self.request_tmdb_type}/now_playing',
               'key': 'results',
               'list_type': '{self.request_tmdb_type}',
               'next_type': '{self.request_tmdb_type}',
               'next_info': 'details',
               },
              'on_the_air':
              {'types': ['tv'],
               'name': 'Currently Airing',
               'path': '{self.request_tmdb_type}/on_the_air',
               'key': 'results',
               'list_type': '{self.request_tmdb_type}',
               'next_type': '{self.request_tmdb_type}',
               'next_info': 'details',
               },
              }

MAINFOLDER = ['search', 'find', 'popular', 'top_rated', 'upcoming', 'airing_today',
              'now_playing', 'on_the_air']