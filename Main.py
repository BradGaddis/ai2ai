from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import LlamaCpp
import infomation as info
from select_model import select_model


# Replace the path with the path to your local model if not using the default
model_path = "./models"

    
if __name__ == "__main__":
    summary_template = """
        Given the information {information} about a person from what I want you to create:
        1. A short summary of the person
        2. Two interesting facts about the person
    """

        # 1. A short summary of the person
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # This is entirely too slow, as is...

    llm = LlamaCpp(model_path=select_model(model_path), verbose=False, max_tokens=1000, n_ctx=2000, n_threads=2)
    # print("llm loaded", llm, end="\n")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    # print(chain)

    print("Running chain...")

    print(chain.run(information=info.test_info))
