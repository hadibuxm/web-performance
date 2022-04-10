def clean_main_json(data):
    keys = data.keys()
    if 'captchaResult' in keys:
        data.pop('captchaResult')
    if 'analysisUTCTimestamp' in keys:
        data.pop('analysisUTCTimestamp')
    if 'kind' in keys:
        data.pop('kind')
    return data

def create_context(data):
    keys = data.keys()
    context = dict()
    
    if 'loadingExperience' in keys:
        context['detailed_loadingexperience'] = data['loadingExperience']
        loading_experience = clean_loading_experience(data)# clean loading experience
        #context.pop('loadingExperience') # delete uncleaned loading experience
        if len(loading_experience) != 0:
            context['loadingExperience'] = loading_experience # add new loading experience
    
    if 'originLoadingExperience' in keys:
        context['detailed_originloadingexperience'] = data['originLoadingExperience']
        origin_loadingexp = clean_origin_loadingexperience(data)
        if len(origin_loadingexp) !=0:
            context['originLoadingExperience'] = origin_loadingexp

    if 'lighthouseResult' in keys:
        context['detailed_lighthouse_experience'] = data['lighthouseResult']
        lighthouse = clean_lighthouse(data['lighthouseResult'])
        if len(lighthouse) != 0:
            context['lighthouseResult'] = lighthouse
    return context

#def clean(data):



def clean_loading_experience(data):
    loadingexperience = dict()
    keys = list()
    if 'metrics' in data['loadingExperience'].keys():
        keys = data['loadingExperience']['metrics'].keys()
    if 'CUMULATIVE_LAYOUT_SHIFT_SCORE' in keys:
        loadingexperience['CUMULATIVE_LAYOUT_SHIFT_SCORE'] = data['loadingExperience']['metrics']['CUMULATIVE_LAYOUT_SHIFT_SCORE']['category']
    if 'FIRST_CONTENTFUL_PAINT_MS' in keys:
        loadingexperience['FIRST_CONTENTFUL_PAINT_MS'] = data['loadingExperience']['metrics']['FIRST_CONTENTFUL_PAINT_MS']['category']
    if 'FIRST_INPUT_DELAY_MS' in keys:
        loadingexperience['FIRST_INPUT_DELAY_MS'] = data['loadingExperience']['metrics']['FIRST_INPUT_DELAY_MS']['category']
    if 'LARGEST_CONTENTFUL_PAINT_MS' in keys:
        loadingexperience['LARGEST_CONTENTFUL_PAINT_MS'] = data['loadingExperience']['metrics']['LARGEST_CONTENTFUL_PAINT_MS']['category']
    if 'overall_category' in data['loadingExperience'].keys():
        loadingexperience['overall_category'] = data['loadingExperience']['overall_category']
    return loadingexperience
    # keys = loading_experience.keys()
    # if 'id' in keys: # remove id from loading
    #     loading_experience.pop('id')
    # if 'initial_url' in keys:
    #     loading_experience.pop('initial_url')
    
    # return loading_experience


def clean_origin_loadingexperience(data):
    origin_loadingexperience = dict()
    keys = data['originLoadingExperience']['metrics'].keys()
    
    if 'CUMULATIVE_LAYOUT_SHIFT_SCORE' in keys:
        origin_loadingexperience['Cumulative Layout Shift Score'] = data['originLoadingExperience'][
            'metrics']['CUMULATIVE_LAYOUT_SHIFT_SCORE']['category']
    if 'FIRST_CONTENTFUL_PAINT_MS' in keys:
        origin_loadingexperience['First Contentful Paint MS'] = data[
            'originLoadingExperience']['metrics']['FIRST_CONTENTFUL_PAINT_MS']['category']
    if 'FIRST_INPUT_DELAY_MS' in keys:
        origin_loadingexperience['First Input Delay MS'] = data[
            'originLoadingExperience']['metrics']['FIRST_INPUT_DELAY_MS']['category']
    if 'LARGEST_CONTENTFUL_PAINT_MS' in keys:
        origin_loadingexperience['Largest Contentful Paint MS'] = data[
            'originLoadingExperience']['metrics']['LARGEST_CONTENTFUL_PAINT_MS']['category']
    if 'overall_category' in data['originLoadingExperience'].keys():
        origin_loadingexperience['overall_category'] = data['originLoadingExperience']['overall_category']
    return origin_loadingexperience


def clean_lighthouse(lighthouse):
    lighthouse_data = dict()
    keys = lighthouse.keys()
    uses_long_cache_ttl_keys = list()
    audits_keys = list()
    if 'fetchTime' in keys:
        lighthouse_data['fetch Time'] = lighthouse['fetchTime']
    if 'audits' in keys:
        audits_keys = lighthouse['audits'].keys()
        lighthouse_data['dom size id'] = lighthouse['audits']['dom-size']['id']
        lighthouse_data['dom size suggetion'] = lighthouse['audits']['dom-size']['title']
        lighthouse_data['dom description'] = lighthouse['audits']['dom-size']['description']
        #lighthouse_data['details'] = lighthouse['audits']['dom-size']['details']
    if 'uses-long-cache-ttl' in audits_keys:
        uses_long_cache_ttl_keys = lighthouse['audits']['uses-long-cache-ttl'].keys()
        lighthouse_data['uses long-cache-ttl title'] = lighthouse['audits']['uses-long-cache-ttl']['title']
        if 'score' in uses_long_cache_ttl_keys:
            lighthouse_data['uses long-cache ttl score'] = lighthouse['audits']['uses-long-cache-ttl']['score']
    # if 'details' in uses_long_cache_ttl_keys:
    #    lighthouse_data['uses-long-cache-ttl_details'] = lighthouse['audits']['uses-long-cache-ttl']['details']
    if 'server-response-time' in audits_keys:
        lighthouse_data['server reponse time title'] = lighthouse['audits']['server-response-time']['title']
        lighthouse_data['server reponse time score'] = lighthouse['audits']['server-response-time']['score']
        #lighthouse_data['server-response-time-details'] = lighthouse['audits']['server-response-time']['details']
    if 'critical-request-chains' in audits_keys:
        lighthouse_data['critical request chains title'] = lighthouse['audits']['critical-request-chains']['title']
        lighthouse_data['critical request chains displayValue'] = lighthouse['audits']['critical-request-chains']['displayValue']
        #lighthouse_data['critical-request-chains-title-details'] = lighthouse['audits']['critical-request-chains']['details']
    if 'uses-optimized-images' in audits_keys:
        lighthouse_data['uses optimized images '] = lighthouse['audits']['uses-optimized-images']['title']
        lighthouse_data['uses optimized images score'] = lighthouse['audits']['uses-optimized-images']['score']
    if 'unsized-images' in audits_keys:
        lighthouse_data['unsized images'] = lighthouse['audits']['unsized-images']['title']
        lighthouse_data['unsized images score'] = lighthouse['audits']['unsized-images']['score']
        #lighthouse_data['unsized-images-details'] = lighthouse['audits']['unsized-images']['details']
    if 'resource-summary' in audits_keys:
        lighthouse_data['resource summary'] = lighthouse['audits']['resource-summary']['title']
        lighthouse_data['resource summary score'] = lighthouse['audits']['resource-summary']['score']
        #lighthouse_data['resource-summary-details'] = lighthouse['audits']['resource-summary']['details']
    if 'render-blocking-resources' in audits_keys:
        lighthouse_data['render blocking resources'] = lighthouse['audits']['render-blocking-resources']['title']
        lighthouse_data['render blocking resources score'] = lighthouse['audits']['render-blocking-resources']['score']
        #lighthouse_data['render-blocking-resources-details'] = lighthouse['audits']['render-blocking-resources']['details']
    # if 'render-blocking-resources' in audits_keys:
    #     lighthouse_data['render-blocking-resources title'] = lighthouse['audits']['render-blocking-resources']['title']
    #     lighthouse_data['render-blocking-resources score'] = lighthouse['audits']['render-blocking-resources']['score']
        #lighthouse_data['render-blocking-resources-details'] = lighthouse['audits']['render-blocking-resources']['details']
    if 'largest-contentful-paint-element' in audits_keys:
        lighthouse_data['largest contentful paint-element'] = lighthouse['audits']['largest-contentful-paint-element']['title']
        #lighthouse_data['largest-contentful-paint-element-details'] = lighthouse['audits']['largest-contentful-paint-element']['details']
    if 'third-party-summary' in audits_keys:
        third_party_summary_keys = lighthouse['audits']['third-party-summary'].keys()
        if 'id' in third_party_summary_keys:
            lighthouse_data['third party summary id'] = lighthouse['audits']['third-party-summary']['id']
        if 'title' in third_party_summary_keys:
            lighthouse_data['third party summary title'] = lighthouse['audits']['third-party-summary']['title']
        if 'description' in third_party_summary_keys:
            lighthouse_data['third-party-summary suggestion'] = lighthouse['audits']['third-party-summary']['description']
        if 'score' in third_party_summary_keys:
            lighthouse_data['third party summary score'] = lighthouse['audits']['third-party-summary']['score']
    if 'uses-optmized-images' in audits_keys:
        uses_optmized_images_keys = lighthouse['audits']['uses-optmized-images'].keys()
        if 'id' in uses_optmized_images_keys:
            lighthouse_data['uses optmized-images id'] = lighthouse['audits']['uses-optmized-images']['id']
        if 'description' in uses_optmized_images_keys:
            lighthouse_data['uses optmized-images description'] = lighthouse['audits']['uses-optmized-images']['description']
        if 'score' in uses_optmized_images_keys:
            lighthouse_data['uses optmized-images score'] = lighthouse['audits']['uses-optmized-images']['score']
        
    if 'legacy-javascript' in audits_keys:
        legacy_javascript_keys = lighthouse['audits']['legacy-javascript'].keys()
        if 'id' in legacy_javascript_keys:
            lighthouse_data['legacy javascript id'] = lighthouse['audits']['legacy-javascript']['id']
        if 'title' in legacy_javascript_keys:
            lighthouse_data['legacy javascript title'] = lighthouse['audits']['legacy-javascript']['title']
        if 'description' in legacy_javascript_keys:
            lighthouse_data['legacy javascript description'] = lighthouse['audits']['legacy-javascript']['description']
        if 'score' in legacy_javascript_keys:
            lighthouse_data['legacy javascript score'] = lighthouse['audits']['legacy-javascript']['score']
    if 'unminified-javascript' in audits_keys:
        unminified_javascriptkeys = lighthouse['audits']['unminified-javascript'].keys()
        if 'id' in unminified_javascriptkeys:
            lighthouse_data['unminified javascript id'] = lighthouse['audits']['unminified-javascript']['id']
        if 'title' in unminified_javascriptkeys:
            lighthouse_data['unminified javascript title'] = lighthouse['audits']['unminified-javascript']['title']
        if 'description' in unminified_javascriptkeys:
            lighthouse_data['unminified javascript description'] = lighthouse['audits']['unminified-javascript']['description']
        if 'score' in unminified_javascriptkeys:
            lighthouse_data['unminified javascript score'] = lighthouse['audits']['unminified-javascript']['score']
    if 'uses-text-compression' in audits_keys:
        uses_text_compression_keys = lighthouse['audits']['uses-text-compression'].keys()
        if 'id' in uses_text_compression_keys:
            lighthouse_data['uses text-compression id'] = lighthouse['audits']['uses-text-compression']['id']
        if 'title' in uses_text_compression_keys:
            lighthouse_data['uses text-compression title'] = lighthouse['audits']['uses-text-compression']['title']
        if 'description' in uses_text_compression_keys:
            lighthouse_data['uses text-compression description'] = lighthouse['audits']['uses-text-compression']['description']
        if 'score' in uses_text_compression_keys:
            lighthouse_data['uses text-compression score'] = lighthouse['audits']['uses-text-compression']['score']
    if 'network-rtt' in audits_keys:
        network_rtt_keys = lighthouse['audits']['network-rtt'].keys()
        if 'id' in network_rtt_keys:
            lighthouse_data['network-rtt id'] = lighthouse['audits']['network-rtt']['id']
        if 'title' in network_rtt_keys:
            lighthouse_data['network-rtt title'] = lighthouse['audits']['network-rtt']['title']
        if 'description' in network_rtt_keys:
            lighthouse_data['network-rtt description'] = lighthouse['audits']['network-rtt']['description']
        if 'score' in network_rtt_keys:
            lighthouse_data['network-rtt score'] = lighthouse['audits']['network-rtt']['score']
    if 'diagnostics' in audits_keys:
        pass
    if 'non-composited-animations' in audits_keys:
        pass
    if 'viewport' in audits_keys:
        pass
    if 'third-party-facades' in audits_keys:
        pass
    if 'user-timings' in audits_keys:
        pass
    if 'uses-rel-preload' in audits_keys:
        pass
    if 'long-tasks' in audits_keys:
        pass
    if 'metrics' in audits_keys:
        pass
    if 'main-thread-tasks' in audits_keys:
        pass
    if 'script-treemap-data' in audits_keys:
        pass
    if 'total-byte-weight' in audits_keys:
        pass
    if '' in audits_keys:
        pass

    return lighthouse_data
    pass
