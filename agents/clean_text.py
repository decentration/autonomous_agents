import re

text = """
this is an AI agent doing financial
0:01
analysis I use it to build an llm link
0:04
chain app that could analyze financial
0:05
statements in fact it's doing it without
0:07
fine-tuning on this 300 Page banking
0:09
annual report right now I'm going to
0:10
teach you how to build it in five
0:11
minutes I went down the rabbit hole to
0:13
discover how to use your own documents
0:14
to build ai-powered large language model
0:16
apps with langchain and the results
0:18
speak for themselves but first of all
0:20
why should we even bother trying to use
0:21
our own documents we've already built
0:23
our own large language model Apple
0:24
streamlit why they need for docos well
0:27
it gives you the ultimate flexibility to
0:28
leverage large language models for tasks
0:30
that are specific to you provide meeting
0:33
minutes and create a summary you could
0:34
upload an assignment outline and have a
0:36
response generated upload an annual
0:37
report and have a large language model
0:39
do the financial analysis for you in
0:42
fact that's what we're going to be doing
0:43
we're going to be building our very own
0:45
personal AI powered investment banker
0:47
using streamlit and our own annual
0:49
report to get started we first need to
0:51
install some dependencies namely Lang
0:52
chain open AI streamlit tick token
0:55
chroma DB Pi PDF and crypto Dome while
0:57
we're at it we're going to need to get
0:59
an open AI API key it's optional to use
1:01
the open AI service you could substitute
1:03
it out for llama CPP or one of the
1:05
hugging face hosted models you want to
1:07
vid on that let me know time to create
1:08
app first up in a new python file called
1:10
app.pi we're going to import some
1:11
initial dependencies OS is going to be
1:13
used to set the API key from
1:15
langchain.lms will import the open AI
1:17
service this will be the core llm we use
1:20
we'll also bring in streamlit while
1:21
we're at it once that's done we can set
1:23
the API key and create the open AI
1:25
Service as an llm if we wanted to we
1:27
could tune the temperature depending on
1:28
how creative or objective we wanted our
1:30
responses we also need somewhere to pass
1:32
the prompt we can use the streamlit.txt
1:34
input element to do this if our user
1:36
hits enter we need a way to send the
1:37
prompt to the llm let's throw in an if
1:39
statement here and write out the text of
1:41
the screen using streamlit.write to
1:42
start the app it's relatively
1:43
straightforward just write streamlit run
1:45
app.pi or whatever your python file is
1:48
named side note all this code is going
1:49
to be available in the description below
1:50
so you can give it a crack yourself this
1:52
gives us a baseline app and uses open AI
1:54
to generate responses but there's one
1:56
key issue here we haven't gone and used
1:58
our own documents yet let's make except
2:00
but before we do a word from our
2:01
sponsors me if you'd like to get up and
2:03
running with python for machine learning
2:04
head over to Godot courses from Nick
2:06
forward slash python where you can take
2:08
my end-to-end tech fundamentals course
2:10
or if you want to dive straight into the
2:12
deep end you can check out my full stack
2:13
machine learning course at this link
2:15
here and use YouTube 50 to get 50 off
2:17
right now back to the video we need to
2:19
bring in some more dependencies so at
2:20
the top of our script we're going to
2:21
bring in pi pdfloader from
2:23
langchain.document loaders and chroma
2:25
from langtain dot Vector stores Pi
2:27
pdfloat is used to load and pass a PDF
2:29
into memory chroma is a vector store
2:31
that is critical to using your own
2:32
documents what actually happens as far
2:34
as I know is your document is tokenized
2:36
and loaded into chroma for querying
2:37
later on this allows you to perform
2:38
similarity search using similarity
2:40
metrics like euclidean distance also
2:43
similar to how Pinecone works we'll do
2:44
this in a sec alright time to load up
2:46
our document using the pi PDF loader
2:48
class we're going to upload a banking
2:49
annual report I've got the files stored
2:51
in the same place as my python script so
2:52
I can just pass the name of the document
2:54
direct to the class if you wanted to use
2:56
your own document you could sub in the
2:58
name of the file here in this case go to
3:00
be a PDF but there are other loaders
3:01
available inside of lanechain we can
3:03
then load the document into chroma using
3:05
the from documents method to do this
3:07
pass the pages from the PDF to the
3:09
loader method and then back to that
3:10
similarity search using a streamlit
3:12
expander class we can search through the
3:13
document in natural text and render the
3:15
results of the screen say we ask about
3:17
the performance of the bank chroma will
3:19
return the relevant passages from the
3:21
document loaded these will eventually be
3:23
passed through to the langchain agent to
3:25
generate a human-like response based on
3:27
that context but we don't need to do
3:28
this manually we can use the vector
3:30
store agent from lanechang this will
3:32
package it all up pretty nicely last set
3:33
of imports home stretch out first up
3:35
we'll import create Vector store agent
3:37
Vector store toolkit and Vector store
3:39
info from
3:40
langchain.agents.agent toolkits the
3:42
vector store info class as far as I can
3:43
tell just provides context about the
3:45
store aka the PDF that we're going to
3:47
pass through to our llm agent you just
3:49
pass through a name description and
3:50
chroma store to that specific class then
3:53
the magic happens we can pass the vector
3:55
store info wrapper to Vector store
3:56
toolkit this makes the PDF available as
3:58
a tool to length similar to how we use
4:01
the Wikipedia toolkit in the langchang
4:02
crash course video and last but not
4:04
least bring it together with the vector
4:05
store agent this is the most critical
4:07
part to the Adrian Creator class we'll
4:09
pass through our original open AI llm
4:11
service and the vector store toolkit
4:13
this packages it all up nicely and will
4:15
in effect give our large language model
4:17
agent access to our PDF rather than just
4:20
outputting responses from the llm like
4:22
we had previously we can now use the
4:23
agent and run the prompt through it and
4:25
again write out the responses to the
4:27
screen this allows us to ask things like
4:29
what was the net profit of the company
4:30
with the response that we're getting
4:32
back from our GPT investment banker
4:34
being
4:34
4706 million or 56 on the prior year
4:38
which just so happens to match Note 6 on
4:40
earnings per share in the notes to the
4:42
financial statements what initiatives
4:44
did the bank take towards sustainability
4:46
our model is calling out the Net Zero
4:48
asset managers initiative and the Net
4:50
Zero Banking online this is pretty
4:52
closely tied to the governance section
4:53
in the financial statement as well and
4:55
last but not least summarize the
4:56
financial performance of the bank
4:58
the model calls out net profit after
5:00
taxes increasing by 56 compared to the
5:03
prior year and EPS increasing by 51 this
5:06
just so happens to match the letter from
5:07
the chair of the board of the
5:08
remuneration committee calling out those
5:10
exact same npat and EPS numbers the
5:13
document used was roughly 300 pages in
5:15
length so documents can take a little
5:16
while to return a response that being
5:18
said in 45 lines of code we've got our
5:20
very own personal investment banker not
5:22
too shabby if you want to check out the
5:23
lane chain crash course video I did go
5:25
and click here


"""

# Remove timestamp lines
cleaned_text = re.sub(r'^\d+:\d+$', '', text, flags=re.MULTILINE)

# Output cleaned text to file
with open('cleaned_text.txt', 'w') as file:
    file.write(cleaned_text)