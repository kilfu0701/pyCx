from enum import Enum

class CxenseURL(Enum):
    DMP_PUSH                           = '/dmp/push'
    DMP_TITLE                          = '/dmp/title'
    DMP_TITLE_UPDATE                   = '/dmp/title/update'
    DMP_TRAFFIC                        = '/dmp/traffic'
    DMP_TRAFFIC_CUSTOM                 = '/dmp/traffic/custom'
    DMP_TRAFFIC_DATA                   = '/dmp/traffic/data'
    DMP_TRAFFIC_EVENT                  = '/dmp/traffic/event'
    DMP_TRAFFIC_USER_HISTOGRAM         = '/dmp/traffic/user/histogram'
    DMP_TRAFFIC_USER_HISTOGRAM_EVENT   = '/dmp/traffic/user/histogram/event'
    DOCUMENT_DELETE                    = '/document/delete'
    DOCUMENT_DESCRIBE                  = '/document/describe'
    DOCUMENT_SEARCH                    = '/document/search'
    DOCUMENT_UPDATE                    = '/document/update'
    PERSISTED                          = '/persisted'
    PERSISTED_CREATE                   = '/persisted/create'
    PERSISTED_DELETE                   = '/persisted/delete'
    PERSISTED_EXECUTE                  = '/persisted/execute'
    PERSISTED_UPDATE                   = '/persisted/update'
    PERSONAL_DELETEREQUEST_CREATE      = '/personal/deleterequest/create'
    PERSONAL_DELETEREQUEST_READ        = '/personal/deleterequest/read'
    PERSONAL_READ                      = '/personal/read'
    PROCESSING_DICTIONARY_CREATE       = '/processing/dictionary/create'
    PROCESSING_DICTIONARY_DELETE       = '/processing/dictionary/delete'
    PROCESSING_DICTIONARY_READ         = '/processing/dictionary/read'
    PROCESSING_DICTIONARY_SEARCH       = '/processing/dictionary/search'
    PROCESSING_DICTIONARY_UPDATE       = '/processing/dictionary/update'
    PROCESSING_LINGUISTICS_EXECUTE     = '/processing/linguistics/execute'
    PROFILE_CONTENT_DELETE             = '/profile/content/delete'
    PROFILE_CONTENT_EXTERNAL_DELETE    = '/profile/content/external/delete'
    PROFILE_CONTENT_EXTERNAL_DELETEALL = '/profile/content/external/deleteAll'
    PROFILE_CONTENT_EXTERNAL_READ      = '/profile/content/external/read'
    PROFILE_CONTENT_EXTERNAL_READALL   = '/profile/content/external/readAll'
    PROFILE_CONTENT_EXTERNAL_UPDATE    = '/profile/content/external/update'
    PROFILE_CONTENT_FETCH              = '/profile/content/fetch'
    PROFILE_CONTENT_PUSH               = '/profile/content/push'
    PROFILE_CONTENT_RELATED            = '/profile/content/related'
    PROFILE_USER                       = '/profile/user'
    PROFILE_USER_EXTERNAL_DELETE       = '/profile/user/external/delete'
    PROFILE_USER_EXTERNAL_LINK         = '/profile/user/external/link'
    PROFILE_USER_EXTERNAL_LINK_LIST    = '/profile/user/external/link/list'
    PROFILE_USER_EXTERNAL_LINK_UPDATE  = '/profile/user/external/link/update'
    PROFILE_USER_EXTERNAL_READ         = '/profile/user/external/read'
    PROFILE_USER_EXTERNAL_STATS        = '/profile/user/external/stats'
    PROFILE_USER_EXTERNAL_UPDATE       = '/profile/user/external/update'
    PROFILE_USER_SEGMENT               = '/profile/user/segment'
    PUBLIC_DATE                        = '/public/date'
    REPORTS_SEARCH                     = '/reports/search'
    REPORTS_SEARCH_USAGE               = '/reports/search/usage'
    SEGMENT_CREATE                     = '/segment/create'
    SEGMENT_DATA_UPDATE                = '/segment/data/update'
    SEGMENT_DELETE                     = '/segment/delete'
    SEGMENT_LOOKALIKE                  = '/segment/lookalike'
    SEGMENT_LOOKALIKE_DETAILS_LIFT     = '/segment/lookalike/details/lift'
    SEGMENT_LOOKALIKE_DETAILS_SIGNALS  = '/segment/lookalike/details/signals'
    SEGMENT_LOOKALIKE_QUALITY          = '/segment/lookalike/quality'
    SEGMENT_LOOKALIKE_UPDATE           = '/segment/lookalike/update'
    SEGMENT_READ                       = '/segment/read'
    SEGMENT_REPORT_COVERAGE            = '/segment/report/coverage'
    SEGMENT_REPORT_OVERLAP             = '/segment/report/overlap'
    SEGMENT_REPORT_REACH               = '/segment/report/reach'
    SEGMENT_UPDATE                     = '/segment/update'
    SITE                               = '/site'
    SITE_CREATE                        = '/site/create'
    SITE_GROUP                         = '/site/group'
    SITE_GROUP_CREATE                  = '/site/group/create'
    SITE_GROUP_UPDATE                  = '/site/group/update'
    SITE_UPDATE                        = '/site/update'
    TRAFFIC                            = '/traffic'
    TRAFFIC_COMPARE                    = '/traffic/compare'
    TRAFFIC_CUSTOM                     = '/traffic/custom'
    TRAFFIC_CUSTOM_DESCRIBE            = '/traffic/custom/describe'
    TRAFFIC_DATA                       = '/traffic/data'
    TRAFFIC_EVENT                      = '/traffic/event'
    TRAFFIC_EVENT_DESCRIBE             = '/traffic/event/describe'
    TRAFFIC_HISTOGRAM_EVENT            = '/traffic/histogram/event'
    TRAFFIC_INTENT                     = '/traffic/intent'
    TRAFFIC_KEYWORD                    = '/traffic/keyword'
    TRAFFIC_KEYWORD_DESCRIBE           = '/traffic/keyword/describe'
    TRAFFIC_RELATED                    = '/traffic/related'
    TRAFFIC_USER                       = '/traffic/user'
    TRAFFIC_USER_EXTERNAL              = '/traffic/user/external'
    TRAFFIC_USER_HISTOGRAM             = '/traffic/user/histogram'
    TRAFFIC_USER_HISTOGRAM_EVENT       = '/traffic/user/histogram/event'
    TRAFFIC_USER_INTEREST              = '/traffic/user/interest'
    TRAFFIC_USER_KEYWORD               = '/traffic/user/keyword'
