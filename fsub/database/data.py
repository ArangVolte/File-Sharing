from tinydb import TinyDB, Query

db = TinyDB('./join_data.json')
Q = Query()

user_data = db.table('cast')
fsub = db.table('fsub')
info = db.table('info')
protect = db.table('protect')
caption_table = db.table('caption')
admin = db.table('admin')

# --- Admin ---
# Mengecek apakah user adalah admin
async def is_admin(user_id: int):
    return admin.contains(Q._id == user_id)

# Menambahkan admin
async def add_admin(user_id: int):
    if not admin.contains(Q._id == user_id):
        admin.insert({'_id': user_id})

# Menghapus admin
async def remove_admin(user_id: int):
    if admin.contains(Q._id == user_id):
        admin.remove(Q._id == user_id)

# Mendapatkan seluruh admin
async def all_admins():
    return [doc['_id'] for doc in admin.all()]

# --- Broadcast ---
def present_user(user_id: int):
    return user_data.contains(Q._id == user_id)

def add_user(user_id: int):
    user_data.insert({'_id': user_id})

def full_userbase():
    return [doc['_id'] for doc in user_data.all()]

def del_user(user_id: int):
    user_data.remove(Q._id == user_id)


# --- FSub ---
async def cek_fsub(chat_id: int):
    return fsub.contains(Q._id == chat_id)

async def add_fsub(chat_id: int):
    fsub.insert({'_id': chat_id})

async def full_fsub():
    return [doc['_id'] for doc in fsub.all()]

async def del_fsub(chat_id: int):
    fsub.remove(Q._id == chat_id)


# --- Info (disable) ---
async def set_disable(user_id: int, disable: bool):
    if info.contains(Q._id == user_id):
        info.update({"disable": disable}, Q._id == user_id)
    else:
        info.insert({"_id": user_id, "disable": disable})

async def get_disable(user_id: int):
    r = info.get(Q._id == user_id)
    return r.get("disable") if r else False


# --- Protect (anti) ---
async def set_protect(user_id: int, anti: bool):
    if protect.contains(Q._id == user_id):
        protect.update({"anti": anti}, Q._id == user_id)
    else:
        protect.insert({"_id": user_id, "anti": anti})

async def get_protect(user_id: int):
    r = protect.get(Q._id == user_id)
    return r.get("anti") if r else True


# --- Caption ---

# Menambah atau memperbarui caption
async def add_caption(user_id: int, caption: str):
    if caption_table.contains(Q._id == user_id):
        caption_table.update({"caption": caption}, Q._id == user_id)
    else:
        caption_table.insert({"_id": user_id, "caption": caption})

# Mengambil caption dari database
async def caption_info(user_id: int):
    r = caption_table.get(Q._id == user_id)
    return r.get("caption") if r else None

# Menghapus caption dari database
async def delete_caption(user_id: int):
    if caption_table.contains(Q._id == user_id):
        caption_table.remove(Q._id == user_id)
