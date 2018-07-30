namespace WordUnscrambler
{
    public class Constants
    {
        public const string WordLookupMethod = "Enter scrambled word(s) manually or as a file: [F] - file, [M] - manual";
        public const string ContinueProgramCheck = "Would you like to continue? [Y]/[N]";

        public const string ScrambledWordsFileReq = "Enter full path including file name: ";
        public const string ScrambledWordsManualReq = "Enter words(s) manually (separated by commas, if multiple): ";
        public const string ScrambleWordsOptionNotRecognized = "The option was not recognized.";

        public const string ErrorScrambledWordsCannotBeLoaded = "Error: Scrambled words cannot be loaded - ";
        public const string ErrorProgramWillBeTerminated = "Error: The program will be terminated - ";

        public const string MatchFound = "Match Found for {0}: {1}";
        public const string MatchNotFound = "No matches have been found";

        public const string Yes = "Y";
        public const string No = "N";
        public const string File = "F";
        public const string Manual = "M";

        public const string WordListFilename = "wordlist.txt";
    }
}
