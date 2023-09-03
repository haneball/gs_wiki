from django.shortcuts import render
from django.http import HttpResponse, Http404
import json
import datetime
import sys
from gw_app.models import Char, BaseAttr, Weapon, Version, GachaPool


# Create your views here.
def get_char_list(request):
    response = {'data': []}
    data = Char.objects.all().order_by('-id')
    if(data):
        for item in data:
            response['data'].append({
                'id': pad_id(item.id, 'char'),
                'name': item.name,
                'star': item.star,
                'element': item.element,
                'type': item.type,
                'area': item.area,
                'description': item.description,
            })
        response['status'] = 200
    else:
        response['status'] = 404
    return HttpResponse(json.dumps(response, ensure_ascii=False), content_type='application/json')


def get_weapon_list(request):
    response = {'data': []}
    data = Weapon.objects.all().order_by('id')
    if(data):
        for item in data:
            response['data'].append({
                'id': pad_id(item.id, 'weapon'),
                'name': item.name,
                'star': item.star,
                'type': item.type,
                'area': item.material_area,
                'description': item.description,
            })
        response['status'] = 200
    else:
        response['status'] = 404
    return HttpResponse(json.dumps(response, ensure_ascii=False), content_type='application/json')


def get_version(request):
    now = datetime.datetime.now()
    version = Version.objects.filter(start_date__lte=now).filter(end_date__gte=now).first()

    response = {
        'number': version.number,
        'name': version.name,
        'start': str(version.start_date),
        'end': str(version.end_date),
        'now': str(now)
    }
    return HttpResponse(json.dumps(response, ensure_ascii=False), content_type='application/json')


def get_gacha_pool(request):
    response = {'data': []}
    now = datetime.datetime.now()
    data = GachaPool.objects.filter(start_date__lte=now).filter(end_date__gte=now)
    
    if(data):
        for item in data:
            response['data'].append({
                'name': item.name,
                'img': item.img,
                'link': item.link
            })
        response['status'] = 200
    else:
        response['status'] = 404
    return HttpResponse(json.dumps(response, ensure_ascii=False), content_type='application/json')


def get_comming_brith(request):
    response = {'data': []}
    today = datetime.date.today()
    start_day = datetime.date(2020, today.month, today.day)
    end_day = start_day + datetime.timedelta(days=60)
    end_day = datetime.date(2020, end_day.month, end_day.day)
    flag_day = datetime.date(2020, 11, 2)

    if(start_day < flag_day):
        # 起始至结束不跨年
        data = Char.objects.filter(brith_date__gte=start_day).filter(brith_date__lte=end_day).order_by('brith_date')
        response['data'] = create_brith_list(data)
    else:
        # 起始至结束需跨年
        data_1 = Char.objects.filter(brith_date__gte=start_day).filter(brith_date__lte='2020-12-31').order_by('brith_date')
        data_2 = Char.objects.filter(brith_date__gte='2020-01-01').filter(brith_date__lte=end_day).order_by('brith_date')
        response['data'] = create_brith_list(data_1) + create_brith_list(data_2)

    if(len(response['data']) > 0):
        response['status'] = 200
    else:
        response['status'] = 404
    return HttpResponse(json.dumps(response, ensure_ascii=False), content_type='application/json')


def query_search(request):
    response = {'data': []}
    keyword = request.GET.get('kw')
    keyword = keyword.encode(encoding='utf-8').decode(encoding='utf-8')
    char_data = Char.objects.filter(name__contains=keyword)
    weapon_data = Weapon.objects.filter(name__contains=keyword)

    if(char_data or weapon_data):
        response['data'] = create_search_list(char_data, 'char', '角色') + create_search_list(weapon_data, 'weapon', '武器')
        response['status'] = 200
    else:
        response['status'] = 404
    return HttpResponse(json.dumps(response, ensure_ascii=False), content_type='application/json')


def query_char(request):
    response = {'data': {}}
    id = int(request.GET.get('id'))
    id -= 10000
    data = Char.objects.get(id=id)
    if(data):
        base_attr = BaseAttr.objects.get(char_id=id)
        talent_info = data.talentinfo_set.order_by('id')
        constellation = data.constellation_set.order_by('id')
        story = data.story_set.order_by('id')
        voice_over = data.voiceover_set.order_by('id')

        response['data']['baseInfo'] = {
            'id': pad_id(data.id, 'char'),
            'name': data.name,
            'title': data.title,
            'star': data.star,
            'element': data.element,
            'type': data.type,
            'area': data.area,
            'brithday': data.brithday,
            'affiliation': data.affiliation,
            'constell': data.constell,
            'description': data.description,
            'bvid': data.bvid,
        }

        base_hp = base_attr.baseHP.split(',')
        base_atk = base_attr.baseATK.split(',')
        base_def = base_attr.baseDEF.split(',')
        ascend_attr = {}
        ascend_attr['label'] = base_attr.ascend_attr_label
        ascend_attr['value'] = base_attr.ascend_attr_value.split(',')
        response['data']['baseAttr'] = {
            'baseHP': base_hp,
            'baseATK': base_atk,
            'baseDEF': base_def,
            'ascendAttr': ascend_attr,
        }

        index = 0
        combat_talent_list = []
        passive_talent_list = []
        for i in range(0, len(talent_info)):
            talent_val = talent_info[i].talentval_set.order_by('id')
            if len(talent_val) <= 0:
                index = i
                break
            attr = []
            for item in talent_val:
                attr.append({
                    'label': item.label,
                    'value': item.value.split(',')
                })
            combat_talent_list.append({
                'title': talent_info[i].title,
                'text': talent_info[i].text,
                'attr': attr
            })

        for i in range(index, len(talent_info)):
            passive_talent_list.append({
                'title': talent_info[i].title,
                'text': talent_info[i].text
            })
        response['data']['combatTalent'] = combat_talent_list
        response['data']['passiveTalent'] = passive_talent_list

        constell_list = []
        for item in constellation:
            constell_list.append({
                'title': item.title,
                'text': item.text,
            })
        response['data']['constellation'] = constell_list

        story_list = []
        for item in story:
            story_list.append({
                'title': item.title,
                'text': item.text,
            })
        response['data']['story'] = story_list

        voice_list = []
        for item in voice_over:
            voice_list.append({
                'title': item.title,
                'text': item.text,
            })
        response['data']['voice'] = voice_list
        response['status'] = 200
    else:
        response['status'] = 404
    return HttpResponse(json.dumps(response, ensure_ascii=False), content_type='application/json')


def query_weapon(request):
    response = {'data': {}}
    id = int(request.GET.get('id'))
    id -= 20000
    weapon = Weapon.objects.get(id=id)
    if(weapon):
        response['data'] = {
            'id': pad_id(weapon.id, 'weapon'),
            'name': weapon.name,
            'star': weapon.star,
            'type': weapon.type,
            'baseATK': weapon.baseATK.split(','),
            'description': weapon.description,
            'story': weapon.story,
        }
        if(int(weapon.star) > 2):
            response['data']['subAttr'] = {
                'label': weapon.sub_label,
                'value': weapon.sub_value.split(','),
            }
            response['data']['effect'] = {
                'title': weapon.effect_title,
                'text': weapon.effect_text.split(',')
            }
        response['status'] = 200
    else:
        response['status'] = 404
    return HttpResponse(json.dumps(response, ensure_ascii=False), content_type='application/json')


def query_material(request):
    if(request.GET.get('day')):
        day = int(request.GET.get('day'))
    else:
        day = datetime.date.today().weekday() + 1
        day = 0 if day == 7 else day
    query_day = day if day <= 3 else day - 3

    response = {'data': [], 'status': 404}
    char_data = Char.objects.filter(material_day=query_day)
    weapon_data = Weapon.objects.filter(material_day=query_day)

    if(char_data and weapon_data):
        char_result = create_material_list(char_data, 'char')
        weapon_result = create_material_list(weapon_data, 'weapon')

        if(sorted(char_result.keys()) == sorted(weapon_result.keys())):
            keys = char_result.keys()
            for k in keys:
                response['data'].append({
                    'area': k,
                    'char': char_result[k],
                    'weapon': weapon_result[k]
                })
            response['status'] = 200
    response['day'] = day
    return HttpResponse(json.dumps(response, ensure_ascii=False), content_type='application/json')


def query_timer(request):
    response = {'data': []}
    today = datetime.date.today()
    category = request.GET.get('category')
    star = request.GET.get('star')
    if(category == 'char'):
        data = Char.objects.filter(star=star)
    elif(category == 'weapon'):
        data = Weapon.objects.filter(star=star)
    
    if(data):
        for item in data:
            if(item.up_start and item.up_end):
                response['data'].append({
                    'id': pad_id(item.id, category),
                    'name': item.name,
                    'debut': item.debut_version,
                    'start': str(item.up_start),
                    'end': str(item.up_end),
                })
        response['today'] = str(today)
        response['status'] = 200
    else:
        response['status'] = 404
    return HttpResponse(json.dumps(response, ensure_ascii=False), content_type='application/json')


"""辅助函数"""
def pad_id(id, category):
    if(category == 'char'):
        id += 10000
    if(category == 'weapon'):
        id += 20000
    return id


def create_brith_list(data):
    result = []
    for item in data:
        result.append({
            'id': pad_id(item.id, 'char'),
            'star': item.star,
            'brithday': item.brithday
        })
    return result


def create_search_list(data, category_en, category_cn):
    result = []
    for item in data:
        result.append({
            'id': pad_id(item.id, category_en),
            'value': item.name,
            'categoryEN': category_en,
            'categoryCN': category_cn
        })
    return result


def create_material_list(data, category):
    result = {}
    for item in data:
        if(not(item.material_area in result)):
            result[item.material_area] = []
        result[item.material_area].append({
            'id': pad_id(item.id, category),
            'star': item.star,
            'type': item.type
        })
    return result
