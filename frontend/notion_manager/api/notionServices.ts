import { Client } from "@notionhq/client"

import * as dotenv from 'dotenv';

// Get environment variables
dotenv.config() 

const notion = new Client({ auth: process.env.NOTION_TOKEN })

const databaseId = process.env.NOTION_DATABASE_ID

async function addItem(title, summary, text ) {
  try {
    const response = await notion.pages.create({
      parent: { database_id: databaseId as string },
      icon: {emoji: "🦎"},
      properties: {
        "Summary": {
          "rich_text":[
            {
              "text": {
                "content": summary
              }
            }
          ]
        },
        title: {
          title:[
            {
              "text": {
                "content": title
              }
            }
          ]
        }
      },
      "children": [
        {
            "object": "block",
            "paragraph": {
                "rich_text": [
                    {
                        "text": {
                            "content": text
                        }
                    }
                ]
            }
        },
    ]
    })
   return response
  } catch (error) {
    return error
  }
}

export default { addItem }