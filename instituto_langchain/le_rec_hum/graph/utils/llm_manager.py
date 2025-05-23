from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

import logging

from instituto_langchain.le_rec_hum.settings import settings

import os, time, re

class LLMManager:
    
    REQUIRED_ENV_VARS = ['GROQ_API_KEY']
    
    def __init__(self):
        """Initializes the LLM manager using the Groq model."""
        self.logger = logging.getLogger(__name__)
        
        self.logger.info("Initializing LLMManager with model deepseek-r1-distill-llama-70b")
        
        self._validate_environment_variables()
        
        try:
            self.llm = ChatGroq(
                model=settings.TTQ_MODEL_NAME,
                api_key=settings.GROQ_API_KEY,
                temperature=0.1,
                max_retries=2,
            )
            self.logger.info("LLM initialized successfully (model: deepseek-r1-distill-llama-70b, temperature: 0.1)\n")
        except Exception as e:
            self.logger.error(f"Error initializing LLM: {str(e)}\n")
            raise Exception(f"LLM initialization failed: {str(e)}")

    def _validate_environment_variables(self) -> None:
        missing_vars = [var for var in self.REQUIRED_ENV_VARS if not os.getenv(var)]
        if missing_vars:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
        
    def invoke(self, prompt: ChatPromptTemplate, **kwargs) -> str:
        """
        Invokes the LLM with the provided prompt and additional parameters.
        
        Args:
            prompt: The chat prompt template
            **kwargs: Variables to format the prompt
            
        Returns:
            str: The model's response
        """
        try:
            start_format_time = time.time()
            messages = prompt.format_messages(**kwargs)
            format_time = time.time() - start_format_time
            
            self.logger.info("Sending request to the model...")
            start_invoke_time = time.time()
            response = self.llm.invoke(messages)
            invoke_time = time.time() - start_invoke_time
           
            response_content = response.content
            self.logger.debug(f"Response received in {invoke_time:.3f}s ({len(response_content)} characters)")
            self.logger.info(f"LLM response: {response_content}")
            
            total_time = format_time + invoke_time
            self.logger.debug(f"Invocation complete. Total time: {total_time:.3f}s")
            
            return re.sub(r'<think>.*?</think>\s*', '', response_content, flags=re.DOTALL)
            
        except Exception as e:
            self.logger.error(f"Error invoking LLM: {str(e)}")
            raise Exception(f"LLM invocation failed: {str(e)}")