import toml

# Load data from inherited_metadata.toml
with open('../inherited_metadata.toml', 'r') as file:
    inherited_data = toml.load(file)

modrinth_path = '../Modrinth/pack.toml'
curseforge_path = '../CurseForge/pack.toml'

# Load data from pack.toml
with open(modrinth_path, 'r') as file:
    modrinth_data = toml.load(file)

# Modify pack.toml with data from inherited_metadata.toml
modrinth_data['name'] = inherited_data['name']
modrinth_data['author'] = inherited_data['author']
modrinth_data['version'] = inherited_data['version']
modrinth_data['versions']['forge'] = inherited_data['forge']
modrinth_data['versions']['minecraft'] = inherited_data['minecraft']

# Write the changes back to pack.toml
with open(modrinth_path, 'w') as file:
    toml.dump(modrinth_data, file)

# Load data from pack.toml
with open(curseforge_path, 'r') as file:
    curseforge_data = toml.load(file)

# Modify pack.toml with data from inherited_metadata.toml
curseforge_data['name'] = inherited_data['name']
curseforge_data['author'] = inherited_data['author']
curseforge_data['version'] = inherited_data['version']
curseforge_data['versions']['forge'] = inherited_data['forge']
curseforge_data['versions']['minecraft'] = inherited_data['minecraft']

# Write the changes back to pack.toml
with open(curseforge_path, 'w') as file:
    toml.dump(curseforge_data, file)
