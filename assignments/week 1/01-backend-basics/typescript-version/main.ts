// Import core decorators and classes from NestJS (a framework similar to FastAPI for TypeScript)
import { Controller, Get, Post, Body, Module } from '@nestjs/common';
import { NestFactory } from '@nestjs/core';

// Define a Data Transfer Object (DTO) to validate the incoming JSON payload (similar to Pydantic's BaseModel)
class MessageDto {
  message: string;
}

// Create a Controller to handle incoming HTTP requests
@Controller()
class AppController {
  // Define a GET route at the "/health" endpoint
  @Get('health')
  health() {
    // Return a simple object, which NestJS automatically converts to JSON
    return { status: 'ok' };
  }

  // Define a POST route at the "/echo" endpoint
  @Post('echo')
  // Extract the JSON body and map it to our MessageDto
  echo(@Body() msg: MessageDto) {
    // Return an object containing the original message
    return { echo: msg.message };
  }
}

// Wrap the controller in a Module, which is required by NestJS to structure the application
@Module({ controllers: [AppController] })
class AppModule {}

// Define an asynchronous function to bootstrap (start) the application
async function bootstrap() {
  // Create the NestJS application instance using our AppModule
  const app = await NestFactory.create(AppModule);
  // Tell the server to listen for incoming traffic on port 8001
  await app.listen(8001);
}
// Execute the bootstrap function to start the server
bootstrap();
