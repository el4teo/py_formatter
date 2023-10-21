import sys

class CodeSection:
    def __init__(self, name, body, key_word, orig_idx, tab_level):
        self.name = name.strip()
        self.body = body
        self.key_word = key_word
        self.orig_idx = orig_idx
        self.tab_level = tab_level

    def __str__(self):
        rep = f"[{self.tab_level}.{self.orig_idx}, '{self.key_word}']: {self.name}"
        return rep
    
    def get_body_as_list_str(self):
        n = len(self.body)
        resp = []
        for i in range(n):
            if type(self.body[i]) == CodeSection:
                resp += self.body[i].get_body_as_list_str()
            else:
                # body[i] is a string
                resp.append(self.body[i])
        return resp

class FomratApplier:
    N_SPACES_TAB = 4
    KEY_WORDS = ['class', 'def']

    def __init__(self, targets):
        self.targets = targets

    @staticmethod
    def read_file(file_name):
        with open(file_name, 'r') as f:
            lines = f.readlines()
        lines = [line.strip('\n') for line in lines]
        return lines
    
    @staticmethod
    def write_file(file_name, lines):
        with open(file_name, 'w') as f:
            for line in lines:
                line = line + "\n"
                f.write(line)
    
    @staticmethod
    def get_tab_lebel(line):
        n_spaces = 0
        for char in line:
            if char == ' ':
                n_spaces += 1
            else:
                break
        if n_spaces == len(line):
            return -1
        else:
            return int(n_spaces/FomratApplier.N_SPACES_TAB)

    @staticmethod
    def has_key_word(line):
        line = line.strip()
        for key_word in FomratApplier.KEY_WORDS:
            if line.startswith(key_word):
                return key_word
        return ''

    @staticmethod
    def split_code(lines, ref_tab_level = 0):
        sections = []
        is_first_time = True
        last_key_word = ''
        body = []
        last_level = 0
        
        for line in lines:
            this_level = FomratApplier.get_tab_lebel(line)
            this_key_word = FomratApplier.has_key_word(line)

            if is_first_time:
                is_first_time = False
                if this_level == ref_tab_level:
                    last_key_word = this_key_word
                    last_level = this_level
                section_idx = 0
                name = line
                body = []
            if this_key_word != '':
                pass
            if this_level == ref_tab_level and this_key_word != '':
                # Old part ended
                if last_key_word == 'class':
                    parts = FomratApplier.split_code(body, ref_tab_level + 1)
                    sections.append(CodeSection(name, parts, last_key_word, section_idx, last_level))
                else:
                    sections.append(CodeSection(name, body, last_key_word, section_idx, last_level))
                # New part begins
                section_idx += 1
                last_key_word = this_key_word
                last_level = this_level
                name = line
                body = []
            body.append(line)   
        # Last section until eof (in case not empty)
        if len(body) == 0:
            return sections
        if last_key_word == 'class':
            parts = FomratApplier.split_code(body)
            sections.append(CodeSection(name, parts, last_key_word, section_idx, last_level))
        else:
            sections.append(CodeSection(name, body, last_key_word, section_idx, last_level))
        return sections

    @staticmethod
    def order_sections_alph(ref_sections):
        list_strings = []
        new_sections = []
        n_secs = len(ref_sections)
        first_added = 0
        for i in range(n_secs):
            if ref_sections[i].orig_idx == 0 and ref_sections[i].key_word == '':
                if ref_sections[i].key_word == 'class':
                    ref_sections[i].body = FomratApplier.order_sections_alph(ref_sections[i].body)
                new_sections.append(ref_sections[i])
                first_added = 1
            elif ref_sections[i].key_word != '':
                list_strings.append(ref_sections[i].name)
                if ref_sections[i].key_word == 'class':
                    ref_sections[i].body = FomratApplier.order_sections_alph(ref_sections[i].body)

        # tuplas (índice, elemento)
        enum_strings = list(enumerate(list_strings))
        enum_strings.sort(key=lambda x: x[1])
        list_idxs = []
        for idx, element in enum_strings:
            list_idxs.append(idx)
            new_sections.append(ref_sections[idx + first_added])
        return new_sections

    def alphabetical_order(self):
        for target in self.targets:
            lines = FomratApplier.read_file(target)
            orig_sections = FomratApplier.split_code(lines)
            new_sections = FomratApplier.order_sections_alph(orig_sections)
            fimal_lines = []
            for section in new_sections:
                fimal_lines += section.get_body_as_list_str()
            FomratApplier.write_file(target, fimal_lines)
            
def main():
    # Check if at least one argument (excluding the script name) is provided
    if len(sys.argv) < 2:
        print("Usage: python script.py target1 [target2 target3 ...]")
        return
    
    targets = []
    for target in sys.argv:
        if target.endswith('.py') == False:
            raise Exception('Works only with python files.')
        targets.append(target)

    formatter = FomratApplier(targets)
    formatter.alphabetical_order()

if __name__ == "__main__":
    main()

# TODO:
# - [ ] Print status of the progress
# - [ ] Function FomratApplier.split_code
#   - [ ] Decorators as part of the section below them
#   - [ ] Code outside 'def' or 'class' considered as a section
# - [ ] Improve format
#   - [ ] Lines with only spaces -> ''
#   - [ ] Two or more consecutive empty lines -> save only one
