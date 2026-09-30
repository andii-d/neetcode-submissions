class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == ['']:
            return ''
        elif strs == []:
            return 'EMPTY'
        
        res = ''
        for word in strs:
            res += f'{len(word)}#{word}'

        return res

    def decode(self, s: str) -> List[str]:
        if s == '':
            return ['']
        elif s == 'EMPTY':
            return []

        res_dec = []
        
        i = 0

        while i < len(s):
            j = i
            
            while s[j] != '#':
                j += 1
                
            
            length = int(s[i:j])

            start = j+1
            cur_word = s[start:start+length]
            res_dec.append(cur_word)
            i = start+length

        return res_dec
                