import { Client } from "@notionhq/client"

import * as dotenv from 'dotenv';

// Get environment variables
dotenv.config() 

const notion = new Client({ auth: process.env.NOTION_TOKEN })

const databaseId = process.env.NOTION_DATABASE_ID

console.log(process.env.NOTION_TOKEN)

console.log(process.env.NOTION_DATABASE_ID)

async function addItem(text) {
  try {
    const response = await notion.pages.create({
      parent: { database_id: databaseId as string },
      properties: {
        title: {
          title:[
            {
              "text": {
                "content": text
              }
            }
          ]
        }
      },
    })
   return response
  } catch (error) {
    return error
  }
}

export default { addItem }