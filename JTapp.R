install.packages("shiny")
install.packages("httr")
install.packages("jsonlite")
install.packages("DT")  
install.packages("rsconnect")


library(httr)
library(jsonlite)
library(shiny)
library(DT)


# 
get_kanji_info <- function(kanji) {
  url <- paste0("https://jisho.org/api/v1/search/words?keyword=", kanji)
  response <- GET(url)
  if (status_code(response) == 200) {
    data <- fromJSON(content(response, "text"))
    return(data$data)
  } else {
    return(NULL)
  }
}
###
ui <- fluidPage(
  titlePanel("Kanji Learning Helper"),
  
  sidebarLayout(
    sidebarPanel(
      textInput("kanji_input", "Enter Kanji:", ""),
      actionButton("search", "Search")
    ),
    
    mainPanel(
      tableOutput("kanji_details"),
      DTOutput("example_sentences")
    )
  )
)
server <- function(input, output, session) {
  kanji_data <- reactiveVal(NULL)
  
  observeEvent(input$search, {
    req(input$kanji_input)
    kanji_info <- get_kanji_info(input$kanji_input)
    
    if (!is.null(kanji_info) && length(kanji_info) > 0) {
      kanji_data(kanji_info[[1]])  # Take the first match
    } else {
      kanji_data(NULL)
    }
  })
  
  output$kanji_details <- renderTable({
    data <- kanji_data()
    if (is.null(data)) return(NULL)
    
    tibble::tibble(
      Kanji = input$kanji_input,
      Reading = paste(data$japanese[[1]]$reading, collapse = ", "),
      Meaning = paste(data$senses[[1]]$english_definitions, collapse = ", ")
    )
  })
  
  output$example_sentences <- renderDT({
    data <- kanji_data()
    if (is.null(data)) return(NULL)
    
    examples <- lapply(data$senses, function(x) x$english_definitions)
    df <- data.frame(Sentence = unlist(examples))
    
    datatable(df, options = list(pageLength = 5))
  })
}
shiny::runApp("JTapp.R")
