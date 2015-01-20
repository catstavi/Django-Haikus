from django.db import models
import nltk
import random
from nltk.corpus import cmudict
from django.db.models.base import ObjectDoesNotExist

# Create your models here.

class Word(models.Model):
    word = models.CharField(max_length=200)
    rhyme_end = models.CharField(max_length=200)
    syllable_count = models.IntegerField(default=0)

    @classmethod
    def load_cmudict(self):
        for number in range(100, 150):
            w_str = cmudict.words()[number]
            w = Word(word = w_str, syllable_count=self.countSyllables(w_str), rhyme_end=self.findRhymeEnd('x'))
            w.save()

    @classmethod
    def countSyllables(self, word):
        try:
            w=Word.objects.get(word=word)
            return w.syllable_count
        except ObjectDoesNotExist:
            phonemeList = cmudict.dict()[word][0]
            syllableCount = 0
            for x in range(len(phonemeList)):
                if self.hasNumber(phonemeList[x]):
                    syllableCount += 1
            w = Word(word = word, syllable_count=syllableCount, rhyme_end="*******")
            w.save()
            return syllableCount

    @classmethod
    # to be implemented later
    def findRhymeEnd(self, phonemeList):
        return "***********"

    @classmethod
    def hasNumber(self, strInput):
        return any(char.isdigit() for char in strInput)

    @classmethod
    def buildLine(self, totalSyllables):
        d = cmudict.dict()
        line = ""
        lineSyllables = 0
        while lineSyllables < totalSyllables:
            syllablesNeeded = totalSyllables-lineSyllables
            word = self.getWordSyllablesLessOrEq(syllablesNeeded)
            line = self.addWord(line, word)
            lineSyllables += self.countSyllables(word)
        return line

    @classmethod
    def getWordSyllablesLessOrEq(self, syllableNum):
        word = random.choice(cmudict.words())
        while self.countSyllables(word) > syllableNum:
            word = random.choice(cmudict.words())
        return word

    @classmethod
    def addWord(self, line, word):
        line += word + " "
        return line
