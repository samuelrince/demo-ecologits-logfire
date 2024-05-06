import logfire
from openai import OpenAI
from ecologits import EcoLogits

EcoLogits.init()

client = OpenAI()

logfire.instrument_openai(client)

response = client.chat.completions.create(
    messages=[{"role": "user", "content": "Tell me a funny joke!"}],
    model="gpt-3.5-turbo"
)

print(f"Energy consumption: {response.impacts.energy.value} kWh")
print(f"GHG emissions: {response.impacts.gwp.value} kgCO2eq")

print("Response:")
print(response.choices[0].message.content)
