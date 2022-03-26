
string1 = "#love #tumblr #memes #quotes #funnytexts #texting #funny #tweets #textpost #texture #frasi #tweegram #tweet #tweetext #tweetexts #texgram #tweedride #instapage #tweembler #frasier #frasitumblr #tweeter #tweemblers #tweeters #frasista #textmessage #frasistas #bhfyp"

sort = string1.split(" ")
sort.sort()
print(" ".join(sort))


string_with_spaces = string1.replace(" ", "").replace("#", " ")
print(string_with_spaces)


dict_nr = dict()
for i in string_with_spaces.split(" "):
    dict_nr[i] = len(i)

print(dict_nr)


string2 = "A hashtag is a metadata tag that is prefaced by the pound sign or hash symbol, # (not to be confused with the pound currency sign). Hashtags are used on microblogging and photo-sharing services such as Twitter, Instagram and WeChat as a form of user-generated tagging that enables cross-referencing of content; that is, sharing a topic or theme. For example, a search within Instagram for the hashtag #bluesky returns all posts that have been tagged with that hashtag. After the initial hash symbol, a hashtag may include letters, digits, and underscores.] The use of hashtags was first proposed by American blogger, product consultant and speaker Chris Messina in a 2007 tweet. Messina made no attempt to patent the use because he felt \"they were born of the internet, and owned by no one\". In 2013, Twitter purportedly told the Wall Street Journal that \"these things are for nerds\" and their use \"wouldn't be adopted widely.\"] By the end of the decade, though, hashtags were entrenched in the culture of the platform, and they soon emerged across Instagram, Facebook, and YouTube. In June 2014, hashtag was added to the Oxford English Dictionary, as \"a word or phrase with the symbol # in front of it, used on social media websites and apps so that you can search for all messages with the same subject\"."

string_with_semicolon = string2.replace(",", ";")
print(string_with_semicolon)

nr_of_in = string_with_semicolon.count("in ")
print(nr_of_in)


set_of_string2 = set(string2)
set_of_string1 = set(string1)
set_of_common_chars = set_of_string1.intersection(set_of_string2)
print(set_of_common_chars)


list_of_sentences_string2 = string2.split(".")

sentence1 = list_of_sentences_string2[0].capitalize()

sentence2 = list_of_sentences_string2[1].upper()

sentence3 = list_of_sentences_string2[2].lower()

sentence4 = list_of_sentences_string2[3].title()


list_of_lower_vowels = ["a", "e", "i", "o", "u", "y"]
list_of_upper_vowels = ["A", "E", "I", "O", "U", "Y"]

sentence5 = ''
for i in list_of_sentences_string2[4]:
    if i in list_of_lower_vowels:
        sentence5 += i.upper()
        continue
    if i in list_of_upper_vowels:
        sentence5 += i.lower()
        continue
    else:
        sentence5 += i

template_whole_sentence = "{}.\n{}.\n{}.\n{}.\n{}."
whole_sentence = template_whole_sentence.format(sentence1, sentence2, sentence3, sentence4, sentence5)
print(whole_sentence)



