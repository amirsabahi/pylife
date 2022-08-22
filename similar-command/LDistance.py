"""Based on Levenshtein Distance Algorithm"""
import math
import traceback


class SimilarCommand():
    """ Find distance """
    COMMAND_LIST = ['init', 'clone', 'config', 'add', 'commit', 'push', 'diff', 'reset', 'status', 'log', 'merge',
                    'rebase', 'rm', 'show', 'tag', 'branch', 'checkout', 'cherry-pick', 'pull', 'stash']

    def find_distance(self, source_txt, target_txt):
        s_length = len(source_txt)
        t_length = len(target_txt)

        if s_length == 0:
            return t_length
        if t_length == 0:
            return s_length

        matrix = [[0] * (s_length+1)] * (t_length+1)  # actually we need a 2D array
        # initialize matrix
        for i in range(t_length+1):
            if i == 0:
                matrix[0] = [n for n in range(0, s_length+1)]

            if i > 0:
                try:

                    matrix[i] = [i] + [0 for n in range(1, s_length+1)]

                except IndexError as e:
                    print('Error:', i, e.__traceback__.tb_frame, e)

        for i in range(s_length):
            char_i_of_source = source_txt[i]
            for j in range(t_length):
                char_j_of_target = target_txt[j]
                try:
                    matrix[i+1][j+1] = min(matrix[i][j+1] + 1, matrix[i+1][j] + 1, matrix[i][j] + int(char_i_of_source != char_j_of_target))
                except IndexError as e:
                    pass


        try:
            result = matrix[t_length - 1][s_length - 1]
        except:
            return 9999
        return result

    def find_command(self, command):
        if command in self.COMMAND_LIST:
            return True
        similarity = {}
        for i in range(len(self.COMMAND_LIST)):
            try:
                similarity[self.COMMAND_LIST[i]] = sd.find_distance(command, self.COMMAND_LIST[i])
            except IndexError as e:
                print('error: ', command, self.COMMAND_LIST[i], traceback.print_exc())
                continue

        result = []
        for key, cmd in similarity.items():
            if cmd == 1:
                result.append(key)
        return result


sd = SimilarCommand()
# print(sd.find_distance('stach', 'stash'))
# print(sd.find_command('ini'))
user_command = input('Enter a git command:')
commands = sd.find_command(user_command)
if isinstance(commands, bool):
    print('Exact command! Execute!')
    exit(1)

if len(commands) < 1:
    print('No Command is Found!')
elif len(commands) == 1:
    print(f'Did you mean {commands[0]}')
else:
    print(f'Did you mean:')
    for cmd in commands:
        print(cmd)