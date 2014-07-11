#import keywords
#from vocabularies_raw import *
from vocabularies import vocabularies

class ConvertVocabularies:
    # Returns list of dictionaries in the following format
    # {'title':'Vocab Name','name':'vocab_name','terms':[{'name':'friendly_name', 'title':'Friendly Name', 'terms'(optional):[{'name':'term_name','title':'Term Name'}]}]}
    @staticmethod
    def convert_raw_vocabularies():
        out_list = []
        # Gather vocabularies to tmp list
        tmp = []
        for vocab in vocabularies:
            # There are two types of vocabularies (lists and dicts) that require different manipulation
            if isinstance(vocabularies[vocab],list):
                tmp = convert_list(vocabularies[vocab])
            elif isinstance(vocabularies[vocab],dict):
                tmp = convert_dict(vocabularies[vocab])
            # Append to output list in required format 
            out_list.append({'title': vocab, 'name': vocab, 'terms': tmp})

        # Do the same for keywords
        tmp = []
        for keyword in keywords:
            tmp.append({'title':keyword, 'name':toMachineFriendly(keyword), 'terms':convert_list(keywords[keyword])})

            # Append to output list in required format 
            # {'title':'Vocab Name','name':'vocab_name','terms':[{'name':'friendly_name', 'title':'Friendly Name'}]}
            out_list.append({'title':'Keywords', 'name':'keywords', 'terms':tmp})

        return out_list

    # Convert human-friendly to machine-friendly names
    @staticmethod
    def toMachineFriendly(name):
        return name.lower().replace(" ","_").replace(",","")

    # Convert each list item to appropriate format
    # {'name':'friendly_name', 'title':'Friendly Name'}
    @staticmethod
    def convert_list(lst):
        lista = []
        inner_dict = {}
        for it in lst:
            lista.append({'name':""+toMachineFriendly(it)+"",'title':""+it+""})
        return lista

    # Convert each dict item to appropriate format
    # {'name':'friendly_name', 'title':'Friendly Name'}
    @staticmethod
    def convert_dict(dct):
        result = []
        for k,v in dct.iteritems():
            result.append({'name': k, 'title':v})
        return result


class Helper:
    def __init__(self):
        pass

    @staticmethod
    def flatten_dict_vals(list):
        result = []
        for i in list:
            if 'name' in i:
                result.append(i['name'])
        return result

    @staticmethod
    def get_keyword_dict(name):
        dict = {}
        for t in vocabularies:
            if t.get('name') == 'keywords':
                for adict in t.get('terms'):
                    if adict.get('name') == name:
                        dict = adict
                        break
            break
        return dict

    @staticmethod
    def get_vocabulary_terms(name):
        outdict = {}
        for adict in vocabularies:
            if adict.get('name') == name:
                outdict = adict
                break
        return outdict.get('terms')

    @staticmethod
    def get_keyword_terms(name):
        outdict = {}
        for adict in vocabularies:
            if adict.get('name') == 'keywords':
                for bdict in adict.get('terms'):
                    if bdict.get('name') == name:
                        outdict = bdict
                        break
                break
        return outdict.get('terms')

    @staticmethod
    def get_keyword_keys():
        lista = []
        for a in vocabularies['keywords']:
            lista.append(a.get('name'))
        return lista
