lines = open("macbeth.txt").read().splitlines()
phrase = "break this enterprise"

first_not_dialog = lambda lines: next(i for i, line in enumerate(lines) if not line.startswith("    "))
get_act = lambda lines: next(i for i, line in enumerate(lines) if  line.startswith("ACT"))
get_scene = lambda lines: next(i for i, line in enumerate(lines) if  line.startswith("SCENE"))

def get_characters(index):
	characters_list = "Characters in scene: "
	for i, line in enumerate(lines):
		if i == index:
			break
		elif (line.startswith("  ") and not line.startswith("    ")):
			if not line.strip() in characters_list:
				if line.strip() != "ALL.":
					characters_list = characters_list + line.strip() + ', '
	return characters_list.replace('.', '')

for i, line in enumerate(lines):
	if phrase in line:
		index = i
		break

dialog_end = index + first_not_dialog(lines[index:])
dialog_start = index - first_not_dialog(lines[index::-1]) + 1

dialog_act_index = index - get_act(lines[index::-1])
dialog_scene_index = index - get_scene(lines[index::-1])

dialog = lines[dialog_start:dialog_end]
dialog_act = lines[dialog_act_index]
dialog_scene = lines[dialog_scene_index]
characters = lines[dialog_start-1].strip()
list_char = get_characters(dialog_scene_index)
print(dialog_act)
print(dialog_scene)
print(list_char)
print("Spoken by:" + characters)
print ("\n".join(line.strip() for line in dialog))
