import random
import re
from collections import defaultdict
import sys

def build_transitions(words, context_size):
    transitions = defaultdict(list)
    # Create transitions for each word up to the given context size
    for i in range(len(words)):
        for size in range(1, context_size + 1):
            if i + size < len(words):
                key = tuple(words[i:i + size])
                next_word = words[i + size]
                transitions[key].append(next_word)
    return transitions

def generate_text(transitions, start_word, num_words, context_size):
    if not transitions:
        return "No transitions available to generate text."
    
    current_context = (start_word,)
    result = list(current_context)
    used_keys = set()  # Keep track of used keys to enhance randomness
    
    for _ in range(num_words - 1):
        if current_context in transitions:
            possible_next_words = transitions[current_context]
            next_word = random.choice(possible_next_words)
            result.append(next_word)
            
            # Update context for the next iteration
            context_length = min(context_size, len(result))
            current_context = tuple(result[-context_length:])
        else:
            # Fallback: choose a random key from transitions if the current context has no valid transition
            available_keys = list(set(transitions.keys()) - used_keys)
            if not available_keys:
                available_keys = list(transitions.keys())
            current_context = random.choice(available_keys)
            result.append(current_context[-1])
            used_keys.add(current_context)
    
    return " ".join(result).replace(" .", ".").replace(" ,", ",").replace(" !", "!").replace(" ?", "?")

def capitalize_text(generated_text):
    # Capitalize the first letter of each sentence and standalone 'i'
    sentences = re.split(r'(\.|!|\?)', generated_text)
    capitalized_sentences = []
    for i in range(0, len(sentences) - 1, 2):
        sentence = sentences[i].strip()
        if sentence:
            capitalized_sentences.append(sentence.capitalize() + sentences[i + 1])
    capitalized_text = ' '.join(capitalized_sentences).strip()
    return re.sub(r'\bi\b', 'I', capitalized_text)

# Sample text and transitions
text = "We are all familiar with the five intertwined circles of the international olympic symbol. They symbolize the fact that we live in an ever smaller, more united and interdependent world. The flag of the International Olympic Committee displays this symbol of society's tremendous progress in communications, international cooperation and other areas of material well-being. It is my experience that many of us do not know how to read the numbers shown on the dials of this electric meter. And even those of us who do rarely stop to think about their significance. Where does electricity, so indispensable for our way of life, come from? Where does energy in general come from? How much energy are we using? How much energy is the world using? Where will our energy come from in the future? How much will it cost? Will all of us be able to afford it? Only 12% of Americans considered energy to be one of the top three national issues. Energy fared below education, rising health costs, crime, deficit, even below national defense. This is perhaps a surprising result, given the fact that energy-related reports appear constantly in the media. It is even more surprising when one considers that energy utilization is so intimately connected with environmental protection and air pollution. As an integral part of the approach that we use at Penn State to teach the course on which this book is based, I ask our students to collect clippings of articles on energy and fuels. I get hundreds of them during unusually hot summers, or unusually cold winters, or when the political situation in the Middle East turns unstable again. But their influx subsides with comfortable weather or as the price of oil comes down from one of its roller coasters. Do the problems exist at all? Do they really disappear as the energy-related headlines give way to other political and economic issues? Therefore, everyone should take an informed stand on the issues of energy supply and demand in the coming years. This applies particularly to those of us who are concerned about the environment and do not realize some of the tradeoffs between energy consumption and air pollution. a In the residential and commercial sector, let's use much more natural gas. It is clean and efficient. Let's also use more solar energy right now. Let's not burn oil in our homes. If and when we run out of cheap gas, let's get the gas from coal. b In the industrial sector, let's continue to burn coal, but let's use the best available technology to minimize pollution. Let's not burn oil in industrial furnaces. c For electricity generation, let's use coal with mandatory exhaust gas cleaning, hydroelectricity and nuclear power. Let's also make sure that the nuclear plants are absolutely safe by running them like a military operation- after all, we are playing with fire in a nuclear reactor. Let's also use more renewable energy in places where the climate is very favorable. Let's not use either oil or natural gas in power plants! d Finally, let's save the oil for the transportation sector. What else can we use that is convenient and inexpensive, at least for now? And let's work more aggressively on alternatives such as natural gas, coal-derived methanol, or fuel cells. For so long, we've had all the eggs in just one basket and we are paying for it dearly. The strategy or the 'policy' that I suggest may be right or wrong, or something between these two extremes. But that's not the important point here. It is debatable and it should be debated. What is important is that it be defended or debated based on facts, and not just on conveniently selected facts or, even worse, on emotions. So in this book we shall emphasize facts. Eventually we shall come back to policy formulation, because that's what the facts are for. But it will be policy formulation at a more authoritative and much more influential level. We shall see that some of these policy statements are more important for what they do not say than for what they do say. It remains to be seen how it will fare in Congress in the coming months or years? In Part I Energy Fundamentals, the facts are laws of nature. Initially, they may be somewhat difficult to grasp, but there is very little controversy about them. We slowly make our way up the somewhat perilous road of elementary thermodynamics toward the central concept in energy use, the efficiency of conversion of one energy form into another. The reward for the diligent and patient reader is very high indeed- it is this concept alone that allows us to make all sorts of simple, interesting and useful back-of-the-envelope calculations that can affect our domestic budget, and we show how it does so. In Part II Energy Supply, the facts are straightforward but they are somewhat more controversial. They are based not only on geological and cosmological information, but also on some economic considerations. We analyze the past, present and future of all energy supply options. What is available? How much is available? What are the virtues and what are the liabilities of the available energy forms? In Part III Energy Demand, the facts are based on statistics. The demand in the past is well documented and we analyze it in some detail. Here we devote significant space to a topic that has been neglected in books and textbooks on energy, and that I consider essential- a quantitative analysis of residential energy bills. It is here that we need no politics to implement policy. Now, that's a luxury! The tools for formulating both technically and economically sound policies at this microeconomic level are shown to be surprisingly easy to grasp and use, and are nonetheless quite effective. In Part IV Summary, the transition from facts to opinions is complete. There are few indisputable statements when politics and economics are brought together with the technical aspects, and indeed when these become dominant. For example, it is well established that natural gas is, in many respects, the ideal residential fuel; yet in many neighborhoods the homeowners do not have this option because the necessary pipelines are not in place. Even though the material covered comes close to the borders of my expertise and to those of a general education textbook, I consider it essential for understanding media reports. Its incorporation is meant to set the stage for an informed debate on energy policies which do need, and inevitably get, a lot of politics. Throughout the text, the relationship between energy consumption and environmental pollution is kept in focus. The second term on the right-hand side of this equation is the per capita income or gross domestic product of a nation. The third and fourth terms are called the energy intensity and the pollution intensity. One does not need a crystal ball to predict that the first term will increase in the foreseeable future, especially in the less developed nations. The second one will also hopefully increase as well. If sustainable or environmentally acceptable economic development is society's goal, rather than economic growth through unlimited resource consumption, one does need a crystal ball to figure out how these increases can be counterbalanced with the necessary decreases in energy and pollution intensities. My ambition is to offer you such a crystal ball, or at least a piece of it. The bills mentioned in the subtitle of the book, and discussed throughout, are both economic and environmental! In the choice of concepts, facts and issues to be included in this introductory course, and especially regarding the depth of their coverage, I needed to be very selective. I wanted to keep the book size within the confines of a one-semester general education course. The selection was thus made with a utilitarian approach, from the perspective of the general reader. The main guideline was to provide an understanding of the issues that are most commonly raised in the media. This is why throughout the text and in the end-of-chapter Investigations, I provide numerous references to, as well as quotes from, newspaper op/ed pages and news reports. The Wilderness Society is asking the readers to support President Clinton's pledge to veto oil and gas drilling there. This is just one illustration of the fact that we are increasingly being asked to take energy-related stands, whether it be on oil drilling or new nuclear power plants or the Kyoto Protocol on greenhouse gas emissions. Numerous simple calculations requiring nothing beyond the four basic operations are also included in the text. They illustrate energy concepts, fuel properties, energy utilization trends and options, and their environmental impact. They are an essential part of this book because they are the basis for much of the decision making. The methodology used in them is more important than the numerical values shown, but I made every effort to use representative numbers. In today's world undergoing a revolution in communications, it is increasingly easy to obtain all sorts of information. Paradoxically, it may be increasingly difficult to know where to find reliable information. Finally, throughout the book I have included essential statistical information on the patterns of energy supply and demand in the U.S. and the world. The reader should inspect these graphs carefully; they are indeed worth a thousand words. In many cases, blank spaces are left on the graphs for the reader to update this information. Keeping track of the recent trends is essential for having the facts straight and for making informed judgments. It is this message - above all others - that I want to convey to the reader of these pages. Note: As mentioned above, throughout the text and especially in end-of-chapter Investigations, I have included references to many newspaper and magazine articles. In the energy arena, what goes around really comes around: the same issues tend to linger for decades and the 'news' about them are often 'recycled'. The ones compiled in the Investigations are thought to be ideal as group projects that can stimulate class discussion. I have not relegated them to footnotes because I consider them essential for my main 'message'."

# Normalize text to lowercase and split words while keeping punctuation separate
words = [token.lower() for token in re.split(r'(\s+|[,.!?;])', text) if token.strip()]

# Accept command line arguments for starting word, number of words, and context size
if len(sys.argv) < 3:
    print("Usage: python3 markov.py <start_word> <num_words> [context_size]")
    sys.exit(1)

start_word = sys.argv[1].lower().strip()
num_words = int(sys.argv[2])
context_size = int(sys.argv[3]) if len(sys.argv) > 3 else 3

# Build transitions
transitions = build_transitions(words, context_size)

# Generate text and capitalize properly
if start_word and transitions:
    generated_text = generate_text(transitions, start_word, num_words, context_size)
    final_output = capitalize_text(generated_text)
    print(final_output)
else:
    print("Could not find a valid start sequence or no transitions available.")

    