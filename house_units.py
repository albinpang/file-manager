
# K = Vänster
# C = Center
# D = Höger
# S = Allmän

# för CM03 ska Side/frame/ext_wall/parent:
#           för vänster ska KS01 + KS10, KS02 + KS04, KS11 + KS13, KS30 + KS(2)30.
# -||-      för center kombineras CS02 + CS04, CS11 + CS13
# -||-      för höger kombineras DS02 + DS04, DS11 + DS13, DS03 + DS12, DS32 + DS(2)32

# För CM03 ska side/frame/LGHA/parent :
#           för vänster kombineras S03 + S12, S32 + S(2)32
#           för center kombineras CS01 + S03, CS10 + S12, CS30 + S32, CS(2)30 + S(2)32
#           för höger kombineras CS01 + CS10, CS30 + CS(2)30
# kombinera side/batten/floor/floor level/parent
# kombinera side/frame/floor/floor level/parent
# kombinera side/batten/roof/dim/parent
# kombinera side/frame/int_wall/dim/floor level/parent
# kombinera side/frame/roof/dim/parent
# kombinera side/frame/roof/top bottom/parent


class House:
    sorting_rules = {}

    def get_categories(self, directory):
        return self.sorting_rules[directory.name]


class Cm03(House):
    sides = ("CENTER", "LEFT", "RIGHT")
    sorting_rules = {
        'CS02': ('CENTER', 'EXT-WALL', 'LEVEL_1'),
        'CS04': ('CENTER', 'EXT-WALL', 'LEVEL_1'),
        'CS11': ('CENTER', 'EXT-WALL', 'LEVEL_2'),
        'CS13': ('CENTER', 'EXT-WALL', 'LEVEL_2'),
        'C1': ('CENTER', 'FLOOR', 'LEVEL_1'),
        'C2': ('CENTER', 'FLOOR', 'LEVEL_1'),
        'C3': ('CENTER', 'FLOOR', 'LEVEL_1'),
        'C4': ('CENTER', 'FLOOR', 'LEVEL_1'),
        'C5': ('CENTER', 'FLOOR', 'LEVEL_1'),
        'C6': ('CENTER', 'FLOOR', 'LEVEL_1'),
        'C7': ('CENTER', 'FLOOR', 'LEVEL_1'),
        'C8': ('CENTER', 'FLOOR', 'LEVEL_1'),
        'C9': ('CENTER', 'FLOOR', 'LEVEL_1'),
        'C10': ('CENTER', 'FLOOR', 'LEVEL_2'),
        'C11': ('CENTER', 'FLOOR', 'LEVEL_2'),
        'C12': ('CENTER', 'FLOOR', 'LEVEL_2'),
        'C13': ('CENTER', 'FLOOR', 'LEVEL_2'),
        'S05': ('RIGHT', 'INT-WALL', 'LEVEL_1'),
        'S06': ('LEFT', 'INT-WALL', 'LEVEL_1'),
        'S07': ('LEFT', 'INT-WALL', 'LEVEL_1'),
        'S08': ('LEFT', 'INT-WALL', 'LEVEL_1'),
        'S09': ('RIGHT', 'INT-WALL', 'LEVEL_1'),
        'S25': ('LEFT', 'INT-WALL', 'LEVEL_1'),
        'S26': ('LEFT', 'INT-WALL', 'LEVEL_1'),
        'S14': ('LEFT', 'INT-WALL', 'LEVEL_2'),
        'S15': ('RIGHT', 'INT-WALL', 'LEVEL_2'),
        'S16': ('LEFT', 'INT-WALL', 'LEVEL_2'),
        'S17': ('RIGHT', 'INT-WALL', 'LEVEL_2'),
        'S18': ('RIGHT', 'INT-WALL', 'LEVEL_2'),
        'S19': ('RIGHT', 'INT-WALL', 'LEVEL_2'),
        'S20': ('LEFT', 'INT-WALL', 'LEVEL_2'),
        'S21': ('RIGHT', 'INT-WALL', 'LEVEL_2'),
        'S22': ('RIGHT', 'INT-WALL', 'LEVEL_2'),
        'S23': ('RIGHT', 'INT-WALL', 'LEVEL_2'),
        'S24': ('RIGHT', 'INT-WALL', 'LEVEL_2'),
        'CS01': ('RIGHT', 'LGHA', 'LEVEL_1'),
        'S03': ('LEFT', 'LGHA', 'LEVEL_1'),
        'CS10': ('RIGHT', 'LGHA', 'LEVEL_2'),
        'S12': ('LEFT', 'LGHA', 'LEVEL_2'),
        'CS(2)30': ('RIGHT', 'LGHA', 'LEVEL_3'),
        'CS30': ('RIGHT', 'LGHA', 'LEVEL_3'),
        'S(2)32': ('LEFT', 'LGHA', 'LEVEL_3'),
        'S32': ('LEFT', 'LGHA', 'LEVEL_3'),
        'CT1': ('CENTER', 'ROOF', None),
        'CT2': ('CENTER', 'ROOF', None),
        'CT3': ('CENTER', 'ROOF', None),
        'CT4': ('CENTER', 'ROOF', None),
        'CT5': ('CENTER', 'ROOF', None),
        'CT6': ('CENTER', 'ROOF', None),

        'KS01': ('LEFT', 'EXT-WALL', 'LEVEL_1'),
        'KS02': ('LEFT', 'EXT-WALL', 'LEVEL_1'),
        'KS04': ('LEFT', 'EXT-WALL', 'LEVEL_1'),
        'KS10': ('LEFT', 'EXT-WALL', 'LEVEL_2'),
        'KS11': ('LEFT', 'EXT-WALL', 'LEVEL_2'),
        'KS13': ('LEFT', 'EXT-WALL', 'LEVEL_2'),
        'KS(2)30': ('LEFT', 'EXT-WALL', 'LEVEL_3'),
        'KS30': ('LEFT', 'EXT-WALL', 'LEVEL_3'),
        'K1': ('LEFT', 'FLOOR', 'LEVEL_1'),
        'K2': ('LEFT', 'FLOOR', 'LEVEL_1'),
        'K3': ('LEFT', 'FLOOR', 'LEVEL_1'),
        'K4': ('LEFT', 'FLOOR', 'LEVEL_1'),
        'K5': ('LEFT', 'FLOOR', 'LEVEL_1'),
        'K6': ('LEFT', 'FLOOR', 'LEVEL_1'),
        'K7': ('LEFT', 'FLOOR', 'LEVEL_1'),
        'K8': ('LEFT', 'FLOOR', 'LEVEL_1'),
        'K9': ('LEFT', 'FLOOR', 'LEVEL_2'),
        'K10': ('LEFT', 'FLOOR', 'LEVEL_2'),
        'K11': ('LEFT', 'FLOOR', 'LEVEL_2'),
        'K12': ('LEFT', 'FLOOR', 'LEVEL_2'),
        'K13': ('LEFT', 'FLOOR', 'LEVEL_2'),
        'KS17': ('LEFT', 'INT-WALL', 'LEVEL_2'),
        'KS22': ('LEFT', 'INT-WALL', 'LEVEL_2'),
        'KT1': ('LEFT', 'ROOF', None),
        'KT2': ('LEFT', 'ROOF', None),
        'KT3': ('LEFT', 'ROOF', None),
        'KT4': ('LEFT', 'ROOF', None),
        'KT5': ('LEFT', 'ROOF', None),
        'KT6': ('LEFT', 'ROOF', None),

        'DS02': ('RIGHT', 'EXT-WALL', 'LEVEL_1'),
        'DS03': ('RIGHT', 'EXT-WALL', 'LEVEL_1'),
        'DS04': ('RIGHT', 'EXT-WALL', 'LEVEL_1'),
        'DS11': ('RIGHT', 'EXT-WALL', 'LEVEL_2'),
        'DS12': ('RIGHT', 'EXT-WALL', 'LEVEL_2'),
        'DS13': ('RIGHT', 'EXT-WALL', 'LEVEL_2'),
        'DS(2)32': ('RIGHT', 'EXT-WALL', 'LEVEL_3'),
        'DS32': ('RIGHT', 'EXT-WALL', 'LEVEL_3'),
        'D1': ('RIGHT', 'FLOOR', 'LEVEL_1'),
        'D2': ('RIGHT', 'FLOOR', 'LEVEL_1'),
        'D3': ('RIGHT', 'FLOOR', 'LEVEL_1'),
        'D4': ('RIGHT', 'FLOOR', 'LEVEL_1'),
        'D5': ('RIGHT', 'FLOOR', 'LEVEL_1'),
        'D6': ('RIGHT', 'FLOOR', 'LEVEL_1'),
        'D7': ('RIGHT', 'FLOOR', 'LEVEL_1'),
        'D8': ('RIGHT', 'FLOOR', 'LEVEL_1'),
        'D9': ('RIGHT', 'FLOOR', 'LEVEL_1'),
        'D10': ('RIGHT', 'FLOOR', 'LEVEL_2'),
        'D11': ('RIGHT', 'FLOOR', 'LEVEL_2'),
        'D12': ('RIGHT', 'FLOOR', 'LEVEL_2'),
        'D13': ('RIGHT', 'FLOOR', 'LEVEL_2'),
        'D14': ('RIGHT', 'FLOOR', 'LEVEL_2'),
        'DS06': ('RIGHT', 'INT-WALL', 'LEVEL_1'),
        'DS07': ('RIGHT', 'INT-WALL', 'LEVEL_1'),
        'DS08': ('RIGHT', 'INT-WALL', 'LEVEL_1'),
        'DS25': ('RIGHT', 'INT-WALL', 'LEVEL_1'),
        'DS26': ('RIGHT', 'INT-WALL', 'LEVEL_1'),
        'DS14': ('RIGHT', 'INT-WALL', 'LEVEL_2'),
        'DS16': ('RIGHT', 'INT-WALL', 'LEVEL_2'),
        'DS20': ('RIGHT', 'INT-WALL', 'LEVEL_2'),
        'DT1': ('RIGHT', 'ROOF', None),
        'DT2': ('RIGHT', 'ROOF', None),
        'DT3': ('RIGHT', 'ROOF', None),
        'DT4': ('RIGHT', 'ROOF', None),
        'DT5': ('RIGHT', 'ROOF', None),
        'DT6': ('RIGHT', 'ROOF', None)}

    folders_to_combine = ["CENTER\\BATTEN\\FLOOR\\", "LEFT\\BATTEN\\FLOOR\\", "RIGHT\\BATTEN\\FLOOR\\",
                          "CENTER\\BATTEN\\ROOF\\", "LEFT\\BATTEN\\ROOF\\", "RIGHT\\BATTEN\\ROOF\\",
                          "CENTER\\FRAME\\FLOOR\\", "LEFT\\FRAME\\FLOOR\\", "RIGHT\\FRAME\\FLOOR\\",
                          "CENTER\\FRAME\\INT_WALL\\", "LEFT\\FRAME\\INT_WALL\\", "RIGHT\\FRAME\\INT_WALL\\",
                          "CENTER\\FRAME\\ROOF\\", "LEFT\\FRAME\\ROOF\\", "RIGHT\\FRAME\\ROOF\\"]

    pairs_to_combine = ['CENTER\\FRAME\\EXT_WALL\\CS02 FRAME', 'CENTER\\FRAME\\EXT_WALL\\CS04 FRAME',
                        'CENTER\\FRAME\\EXT_WALL\\CS11 FRAME', 'CENTER\\FRAME\\EXT_WALL\\CS13 FRAME',
                        'LEFT\\FRAME\\EXT_WALL\\KS01 FRAME', 'LEFT\\FRAME\\EXT_WALL\\KS10 FRAME',
                        'LEFT\\FRAME\\EXT_WALL\\KS02 FRAME', 'LEFT\\FRAME\\EXT_WALL\\KS04 FRAME',
                        'LEFT\\FRAME\\EXT_WALL\\KS11 FRAME', 'LEFT\\FRAME\\EXT_WALL\\KS13 FRAME',
                        'LEFT\\FRAME\\EXT_WALL\\KS30 FRAME', 'LEFT\\FRAME\\EXT_WALL\\KS(2)30 FRAME']


class Cm06(House):
    sides = None
    sorting_rules = {
        "S01": (None, "EXT_WALL", "LEVEL_1"),
        "S02": (None, "EXT_WALL", "LEVEL_1"),
        "S03": (None, "EXT_WALL", "LEVEL_1"),
        "S04": (None, "EXT_WALL", "LEVEL_1"),

        "S10": (None, "EXT_WALL", "LEVEL_2"),
        "S11": (None, "EXT_WALL", "LEVEL_2"),
        "S12": (None, "EXT_WALL", "LEVEL_2"),
        "S13": (None, "EXT_WALL", "LEVEL_2"),
        "S(2)11": (None, "EXT_WALL", "LEVEL_2"),
        "S(2)13": (None, "EXT_WALL", "LEVEL_2"),

        'P1': (None, 'FLOOR', None),
        'P2': (None, 'FLOOR', None),
        'P3': (None, 'FLOOR', None),
        'P4': (None, 'FLOOR', None),
        'P5': (None, 'FLOOR', None),
        'P6': (None, 'FLOOR', None),

        'S05': (None, 'INT_WALL', 'LEVEL_1'),
        'S06': (None, 'INT_WALL', 'LEVEL_1'),
        'S07': (None, 'INT_WALL', 'LEVEL_1'),
        'S08': (None, 'INT_WALL', 'LEVEL_1'),
        'S09': (None, 'INT_WALL', 'LEVEL_1'),
        'S29': (None, 'INT_WALL', 'LEVEL_1'),
        'S30': (None, 'INT_WALL', 'LEVEL_1'),

        'S14': (None, 'INT_WALL', 'LEVEL_2'),
        'S15': (None, 'INT_WALL', 'LEVEL_2'),
        'S16': (None, 'INT_WALL', 'LEVEL_2'),
        'S17': (None, 'INT_WALL', 'LEVEL_2'),
        'S18': (None, 'INT_WALL', 'LEVEL_2'),
        'S19': (None, 'INT_WALL', 'LEVEL_2'),
        'S20': (None, 'INT_WALL', 'LEVEL_2'),
        'S21': (None, 'INT_WALL', 'LEVEL_2'),
        'S22': (None, 'INT_WALL', 'LEVEL_2'),
        'S23': (None, 'INT_WALL', 'LEVEL_2'),
        'S24': (None, 'INT_WALL', 'LEVEL_2'),
        'S25': (None, 'INT_WALL', 'LEVEL_2'),
        'S26': (None, 'INT_WALL', 'LEVEL_2'),
        'S27': (None, 'INT_WALL', 'LEVEL_2'),
        'S28': (None, 'INT_WALL', 'LEVEL_2'),

        'st1': (None, 'ROOF', None),
        'st2': (None, 'ROOF', None),
        'st3': (None, 'ROOF', None),
        'st4': (None, 'ROOF', None),
        'st5': (None, 'ROOF', None),
        'st6': (None, 'ROOF', None),
        'st7': (None, 'ROOF', None),
        'st8': (None, 'ROOF', None),
        'st9': (None, 'ROOF', None),
        'st10': (None, 'ROOF', None)
    }

    """
    folders_to_combine = [Path(path) for path in ["BATTEN\\FLOOR\\", "FRAME\\FLOOR\\"]]
    folders_to_combine.extend(Path("BATTEN\\ROOF\\").iterdir())
    folders_to_combine.extend(Path("FRAME\\ROOF\\").iterdir())
    [folders.extend(list_dir(folder)) for folder in list_dir("FRAME\\INT_WALL\\"))]

    pairs_to_combine = list()
    pairs_to_combine.append([fr"{self.source_root}\FRAME\EXT_WALL\S01 FRAME", fr"{self.source_root}\FRAME\EXT_WALL\S03 FRAME"])
    pairs_to_combine.append([fr"{self.source_root}\FRAME\EXT_WALL\S02 FRAME", fr"{self.source_root}\FRAME\EXT_WALL\S04 FRAME"])
    pairs_to_combine.append([fr"{self.source_root}\FRAME\EXT_WALL\S10 FRAME", fr"{self.source_root}\FRAME\EXT_WALL\S12 FRAME"])
    pairs_to_combine.append([fr"{self.source_root}\FRAME\EXT_WALL\S11 FRAME", fr"{self.source_root}\FRAME\EXT_WALL\S13 FRAME"])
    pairs_to_combine.append([fr"{self.source_root}\FRAME\EXT_WALL\S(2)11 FRAME", fr"{self.source_root}\FRAME\EXT_WALL\S(2)13 FRAME"])
    """
