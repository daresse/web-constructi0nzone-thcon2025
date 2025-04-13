import sqlite3

def init_db():
    co = sqlite3.connect("agents.db")
    cursor = co.cursor()

    # INITIATE TABLES (roles can be agent or admin)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            agent_id INTEGER NOT NULL, 
            username TEXT NOT NULL, 
            password TEXT NOT NULL, 
            role TEXT NOT NULL,  
            PRIMARY KEY (agent_id)
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS missions (
            mission_id INTEGER NOT NULL, 
            title TEXT NOT NULL, 
            descriptions TEXT NOT NULL, 
            associated_agents TEXT NOT NULL, 
            PRIMARY KEY (mission_id)
        );
    """)

    # MISSION DATAS
    mission_titles = ["Il faut sauver le soldat Blackwood", "Infiltration JJJ", "appocalIA"]
    mission_desc = [
        "Caspian Blackwood, on ne sait toujours pas ce qu'il est devenu. Objectif : aller faire un tour chez les autres gangs de la ville pour voir s'ils ont des informations. Nous avons les moyens de les faire parler.",
        "Johnny John Johnson, Jeune cadre dynamique en télétravail chez Aurora Initiative pourrait avoir des informations croustillantes. Objectif : prendre le contrôle de son materiel informatique pour le faire chanter, utiliser la force si impossible.",
        "La situation est encore trop stable pour mettre en place notre plan final. Objectif : Semer le trouble..."
    ]
    associated_agents = ["1", "0, 2", "3"]

    # AGENT DATAS
    agent_usernames = ["Dimitri Ieba","Mikhail Petrov", "Kato Reyes", "Gunnar Olson", "THC{WTF_1S","_V3rIFying_US3R_INP#T}"]
    agent_pwd = [
        "cd5deab373d3d8ed45ea17ce911a9277","572ee0f5459ee5ac4ae2bb6520e0c0f9", "572ee0f5459ee5ac4ae2bb6520e0c0f9",
        "9735de58bdc02ad95b6f233c859f98f9", "63b367f32cd875f192aac32b7d694b2b", "c0bad39b8295f3b3df551fe34ba46ed5"
    ]
    agent_roles = ["admin", "member", "member", "member", "member","member"]  # permission management

    # FILL TABLES WITH DATA 
    for i in range(len(mission_titles)):
        cursor.execute("""
            INSERT OR IGNORE INTO missions (mission_id, title, descriptions, associated_agents) 
            VALUES (?, ?, ?, ?)
        """, (i, mission_titles[i], mission_desc[i], associated_agents[i]))

    for i in range(len(agent_usernames)):
        cursor.execute("""
            INSERT OR IGNORE INTO users (agent_id, username, password, role) 
            VALUES (?, ?, ?, ?)
        """, (i, agent_usernames[i], agent_pwd[i], agent_roles[i]))
    
    co.commit()
