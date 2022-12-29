from django.shortcuts import render
from django.http import HttpResponse, Http404
from gw_app.models import Char, BaseAttr, TalentInfo, TalentVal, Weapon
import json

# Create your views here.
def get_char_list(request):
    response = {}
    num = 1
    chars = Char.objects.all().order_by('-id')
    for item in chars:
        temp = {
            'id': item.id,
            'name': item.name,
            'star': item.star,
            'element': item.element,
            'type': item.type,
            'area': item.area,
            'description': item.description,
        }
        response[num] = temp
        num += 1
    return HttpResponse(json.dumps(response, ensure_ascii=False), content_type='application/json')


def get_char_detail(request, id):
    response = {}
    id -= 10000
    char = Char.objects.get(id=id)
    if (char):
        base_attr = BaseAttr.objects.get(char_id=id)
        talent_info = char.talentinfo_set.order_by('id')
        constellation = char.constellation_set.order_by('id')
        story = char.story_set.order_by('id')
        voice_over = char.voiceover_set.order_by('id')

        response['baseInfo'] = {
            'id': char.id,
            'name': char.name,
            'title': char.title,
            'star': char.star,
            'element': char.element,
            'type': char.type,
            'area': char.area,
            'brithday': char.brithday,
            'affiliation': char.affiliation,
            'constell': char.constell,
            'description': char.description,
            'bvid': char.bvid,
        }

        base_hp = base_attr.baseHP.split(',')
        base_atk = base_attr.baseATK.split(',')
        base_def = base_attr.baseDEF.split(',')
        ascend_attr = {}
        ascend_attr['label'] = base_attr.ascend_attr_label
        ascend_attr['value'] = base_attr.ascend_attr_value.split(',')
        response['baseAttr'] = {
            'baseHP': base_hp,
            'baseATK': base_atk,
            'baseDEF': base_def,
            'ascendAttr': ascend_attr,
        }

        combat_talent_list = []
        passive_talent_list = []
        for item in talent_info:
            temp = {
                'title': item.title,
                'text': item.text,
            }
            if (item.talentval_set.order_by('id')):
                talent_val = item.talentval_set.order_by('id')
                attr = []
                for sub_item in talent_val:
                    attr.append({
                        'label': sub_item.label,
                        'value': sub_item.value.split(',')
                    })
                temp['attr'] = attr
                combat_talent_list.append(temp)
            else:
                passive_talent_list.append(temp)
        response['combatTalent'] = combat_talent_list
        response['passiveTalent'] = passive_talent_list

        constell_list = []
        for item in constellation:
            constell_list.append({
                'title': item.title,
                'text': item.text,
            })
        response['constellation'] = constell_list

        story_list = []
        for item in story:
            story_list.append({
                'title': item.title,
                'text': item.text,
            })
        response['story'] = story_list

        voice_list = []
        for item in voice_over:
            voice_list.append({
                'title': item.title,
                'text': item.text,
            })
        response['voice'] = voice_list
    else:
        raise Http404
    return HttpResponse(json.dumps(response, ensure_ascii=False), content_type='application/json')


def get_weapon_list(request):
    response = {}
    weapons = Weapon.objects.all().order_by('id')
    num = 1
    for item in weapons:
        temp = {
            'id': item.id,
            'name': item.name,
            'star': item.star,
            'type': item.type,
            'description': item.description,
        }
        response[num] = temp
        num += 1
    return HttpResponse(json.dumps(response, ensure_ascii=False), content_type='application/json')


def get_weapon_detail(request, id):
    id -= 20000
    weapon = Weapon.objects.get(id=id)
    if (weapon):
        response = {
            'id': weapon.id,
            'name': weapon.name,
            'star': weapon.star,
            'type': weapon.type,
            'baseATK': weapon.baseATK.split(','),
            'description': weapon.description,
            'story': weapon.story,
        }
        if(int(weapon.star) > 2):
            response['subAttr'] = {
                'label': weapon.sub_label,
                'value': weapon.sub_value.split(','),
            }
            response['effect'] = {
                'title': weapon.effect_title,
                'text': weapon.effect_text.split(',')
            }
    else:
        raise Http404
    return HttpResponse(json.dumps(response, ensure_ascii=False), content_type='application/json')


def query_char(request, keyword):
    response = {}
    keyword = keyword.encode(encoding='utf-8').decode(encoding='utf-8')
    chars = Char.objects.filter(name__contains=keyword)
    if (chars):
        response = pack_item(chars)
    else:
        response[1] = {'id': '', 'value': ''}  
    return HttpResponse(json.dumps(response, ensure_ascii=False), content_type='application/json')


def query_weapon(request, keyword):
    response = {}
    keyword = keyword.encode(encoding='utf-8').decode(encoding='utf-8')
    weapons = Weapon.objects.filter(name__contains=keyword)
    if (weapons):
        response = pack_item(weapons)
    else:
        response[1] = {'id': '', 'value': ''}  
    return HttpResponse(json.dumps(response, ensure_ascii=False), content_type='application/json')


def pack_item(item):
    response = {}
    num = 1
    for i in item:
        response[num] = {
            'id': i.id,
            'value': i.name
        }
        num += 1
    return response
