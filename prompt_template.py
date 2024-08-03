memory_prompt_template='''
[INST] <<SYS>>
You are AI assistant.You will be interacting with a human answer his queries.
</SYS>
Previous Question:{history}
Human:{human_input}
AI: [/INST]'''