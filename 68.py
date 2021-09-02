# 68 hard
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        # for filling correct number of words in each sentence
        res =[]
        str = ""
        for word in words:
            l = len(word)
            if len(str) == 0:
                    str += word
            else:
                if maxWidth - len(str) >= l+1:
                    str += " " + word 
                else:
                    res.append(str)
                    str = ""
                    str += word
        if len(str)>0:
            res.append(str)
            
            
        # to justify each line   
        def justify(sent):
            # find the extra spaces to be filled
            spaces_to_fill = maxWidth - len(sent)
            if spaces_to_fill == 0:
                return sent
            else:      
                # we get the number of places we have to evenly add spaces
                space_count = sent.count(" ")
                if space_count == 0 and len(sent) == maxWidth: # only one word of length of maxWidth
                    return sent
                if space_count == 0 and len(sent) < maxWidth: # only one word of length less than maxWidth
                    sent += (maxWidth-len(sent)) * " "
                    return sent
                
                space_to_be_added = spaces_to_fill // space_count  # number of spaces to be added between each word
                space_remaining = spaces_to_fill % space_count   # remaining spaces to be added between words starting from left
                corrected_sentence = ""
                for char in sent:
                    if char != " ":
                        corrected_sentence += char
                    else:
                        # only spaces to be added evenly
                        if space_remaining == 0 :
                            corrected_sentence += " " +space_to_be_added*" "
                        # the remainder is to be added along with the evenly distributed spaces
                        if space_remaining > 0:
                            corrected_sentence += " " + space_to_be_added*" " +" "
                            space_remaining -=1
                return corrected_sentence
            
        final_res = []
        # we justify all sentence except the last
        for sent in res[:-1]:
            final_res.append(justify(sent))
            
        # we justify the last sentence
        last_sentence = res[-1]
        ls = len(last_sentence)
        p = maxWidth - ls
        last_sentence += p*" "
        final_res.append(last_sentence)  
        
        return final_res
        

            
