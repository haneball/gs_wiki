import request from "../utils/request"

export const getCharList = () => request.get('/char/list')

export const getWeaponList = () => request.get('/weapon/list')

export const getVersion = () => request.get('/version')

export const getGachaPool = () => request.get('/gacha_pool')

export const getComingBrith = () => request.get('/comming_brith')

export const querySearch = (kw) => request.get(`/search?kw=${encodeURI(kw)}`)

export const queryChar = (id) => request.get(`/char/detail?id=${id}`)

export const queryWeapon = (id) => request.get(`/weapon/detail?id=${id}`)

export const queryMaterial = (day='') => request.get('/material?day=' + day)

export const queryTimer = (category, rate) => request.get(`/timer?category=${category}&star=${rate}`)
