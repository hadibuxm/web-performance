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
        loading_experience = clean_loading_experience(data)# clean loading experience
        #context.pop('loadingExperience') # delete uncleaned loading experience
        context['loadingExperience'] = loading_experience # add new loading experience
    
    if 'originLoadingExperience' in keys:
        original_loadingexp = clean_original_loadingexperience(data['originLoadingExperience'])
        context.update(original_loadingexp)

    if 'lighthouseResult' in keys:
        lighthouse = clean_lighthouse(data['lighthouseResult'])
        context.update(lighthouse)
    return context

#def clean(data):



def clean_loading_experience(data):
    loadingexperience = dict()
    loadingexperience['CUMULATIVE_LAYOUT_SHIFT_SCORE'] = data['loadingExperience']['metrics']['CUMULATIVE_LAYOUT_SHIFT_SCORE']['category']
    loadingexperience['FIRST_CONTENTFUL_PAINT_MS'] = data['loadingExperience']['metrics']['FIRST_CONTENTFUL_PAINT_MS']['category']
    loadingexperience['FIRST_INPUT_DELAY_MS'] = data['loadingExperience']['metrics']['FIRST_INPUT_DELAY_MS']['category']
    loadingexperience['LARGEST_CONTENTFUL_PAINT_MS'] = data['loadingExperience']['metrics']['LARGEST_CONTENTFUL_PAINT_MS']['category']
    loadingexperience['overall_category'] = data['loadingExperience']['overall_category']
    return loadingexperience
    # keys = loading_experience.keys()
    # if 'id' in keys: # remove id from loading
    #     loading_experience.pop('id')
    # if 'initial_url' in keys:
    #     loading_experience.pop('initial_url')
    
    # return loading_experience


def clean_original_loadingexperience(original_loadingexp):
    return original_loadingexp
    pass


def clean_lighthouse(lighthouse):
    return lighthouse
    pass
