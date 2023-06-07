import { Client } from "@notionhq/client"

import * as dotenv from 'dotenv';

// Get environment variables
dotenv.config() 

const notion = new Client({ auth: process.env.NOTION_TOKEN })

const databaseId = process.env.NOTION_DATABASE_ID

async function addItem(timestamp: string, title: string, summary: string, text: string, score: number) {
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
        "Time": {
          "rich_text":[
            {
              "text": {
                "content": timestamp
              }
            }
          ]
        },
        "Importance Score": {
          "type": "number",
          "number": score
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