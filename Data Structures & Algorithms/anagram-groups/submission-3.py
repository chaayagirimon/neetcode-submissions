class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dict = {}
        final_list = []
        sublist = []
        for n, s in enumerate(strs):
            sort = ''.join(sorted(s))
            if sort in sorted_dict:
                index = sorted_dict.get(sort)
                for sub_list in final_list:
                    if strs[index] in sub_list:
                        sub_list.append(s)
            else:
                sorted_dict[sort] = n
                final_list.append([s])
        return final_list
            
