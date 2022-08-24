"""Based on Jaro Similarity Algorithm"""
import math


class Similarity:
    def intersection(self, list1, list2):
        intersection = [value for value in list1 if value in list2]
        return intersection

    def calculate_similarity(self, source, target):
        source_txt = source
        target_txt = target
        source_list = list(source_txt)
        source_length = len(source_txt)
        target_list = list(target_txt)
        target_length = len(target_txt)
        # Same String
        if source_txt == target_txt:
            return 1

        m = len(self.intersection(source_list, target_list))
        # m is the number of matching characters

        if m == 0:
            return 0  # No similarity

        max_distance = (max(source_length, target_length) // 2) - 1
        diff = abs(source_length - target_length)
        min_length = min(source_length, target_length)

        # the number of characters that are not in order
        hash_source = [0] * source_length
        hash_target = [0] * target_length
        match = 0.0

        # Check characters in string one alphabet by alphabet
        for i in range(source_length):
            # Check if there is any matches
            # Start from 0 up to max_distance  till the length of target source or till the max distance +1
            for j in range(max(0, i - max_distance),
                           min(target_length, i + max_distance + 1)):

                # If there is a match add 1 to the hash of both strings and add one to match
                if source_txt[i] == target_txt[j] and hash_target[j] == 0:
                    hash_source[i] = 1
                    hash_target[j] = 1
                    match += 1
                    break

        # No match so return 0.0
        if match == 0:
            return 0.0

        # Calculate number of transpositions
        transpositions = 0
        point = 0

        # Find disposition matching characters
        for i in range(source_length):
            if hash_source[i]:
                while hash_target[point] == 0:
                    point += 1

                if source_txt[i] != target_txt[point]:
                    transpositions += 1
                point += 1

        transpositions = transpositions // 2

        # Jaro similarity can be calculated :
        similarity = 1 / 3 * ((m / source_length) + (m / target_length) + ((m - transpositions) / m))
        return similarity

    def find_command(self, user_cmd):
        COMMAND_LIST = ['init', 'clone', 'config', 'add', 'commit', 'push', 'diff', 'reset', 'status', 'log', 'merge',
                        'rebase', 'rm', 'show', 'tag', 'branch', 'checkout', 'cherry-pick', 'pull', 'stash']
        largest = 0.0
        correct_command = ''
        for cmd in COMMAND_LIST:
            similarity_score = s.calculate_similarity(user_cmd, cmd)
            if largest < similarity_score:
                largest = similarity_score
                correct_command = cmd
        if correct_command == user_cmd:
            print(f'It is correct CMD\n')
            return
        print(f'Did you mean: \n \t {correct_command}')


s = Similarity()
# print(s.calculate_similarity('abc', 'bac'))

cmd = input('Enter a git command (No git at the beginning): ')
s.find_command(cmd)
