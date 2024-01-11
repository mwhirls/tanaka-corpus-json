# tanaka-corpus-json

[![stability-wip](https://img.shields.io/badge/stability-wip-lightgrey.svg)](https://github.com/mkenney/software-guides/blob/master/STABILITY-BADGES.md#work-in-progress)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 
[![CC BY 4.0][cc-by-shield]][cc-by] 

Japanese example sentences from the [Tanaka Corpus](https://www.edrdg.org/wiki/index.php/Tanaka_Corpus) (now maintained by the Tatoeba Project) in JSON format.

## Format

Each sentence entry in the JSON contains:
* The entry ID, corresponding to the Japanese example sentence ID from Tatoeba
* The Japanese example sentence from Tatoeba
* The corresponding English translation provided by Tatoeba
* A list of words that appear in the sentence containing:
  * The headword form (dictionary form)
  * An optional reading
  * An optional sense index (which refers to correct sense for the word's dictionary entry in jmdict)
  * An optional surface form, if this differs from the headword form
  * An optional field ("checked") indicating that the sentence pair is a good and checked example of the usage of the word
 
The list of words for each example sentences is provided by Tatoeba under  [<b>Japanese indices</b>](https://tatoeba.org/en/downloads).  The indices were originally compiled when the corpus was integrated into the WWWJDIC server as detailed in the this [publication](https://www.edrdg.org/~jwb/paperdir/dicexamples.html).

See [here](https://dict.longdo.com/about/hintcontents/tanakacorpus.html) for more information on the original data format of the Tanaka Corpus.

## Releases

You can download the pre-built JSON files from the [latest release](https://github.com/mwhirls/tanaka-corpus-json/releases/latest).  Automated releases containing the latest example sentences are scheduled weekly.

## License

### Tanaka Corpus

The Tanaka Corpus is now maintained within the [Tatoeba Project](https://tatoeba.org/en/downloads).  All files downloaded through the Tatoeba Project are licensed under the [CC BY 2.0 FR license][cc-by].

As required by the original license, all derived files containing example sentences distributed in each release are made available under the same license.

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: https://creativecommons.org/licenses/by/2.0/fr/deed.en
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

### Source Code
The original source code and other files in this project, excluding the files mentioned above, are made available under the MIT license (see [LICENSE.txt](LICENSE.txt)).
