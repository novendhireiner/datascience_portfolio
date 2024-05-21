#---------------------------------------------------------------------------#
# Libraries
#---------------------------------------------------------------------------#

library(shiny)
library(palmerpenguins)
library(tidyr)
library(dplyr)
library(ggplot2)

#---------------------------------------------------------------------------#
# User Interface
#---------------------------------------------------------------------------#

penguins <- na.omit(penguins)


## Define a UI
### Typen des UI: Einmal die Fluidpage (die benutzt du 99.9 %)
### Staticpage: Muss alles manuell platzieren

ui <- fluidPage(

  titlePanel("Interactive Box plot"),

  mainPanel(
    plotOutput("Pinguinplot")
  ),

  #sidebarPanel(
  #  sliderInput("weight", # Input variable
  #              "Weight of Penguins: ", # Titel der Variable
  #              min = min(penguins$body_mass_g), # Minimal value of body mass g
  #              max = max(penguins$body_mass_g),
  #              value = c(min(penguins$body_mass_g), max(penguins$body_mass_g))
                
  sidebarPanel(
    sliderInput("length", # Input variable
                "Length of Penguin's Flipper: ", # Titel der Variable
                min = min(penguins$flipper_length_mm), # Minimal value of flipper length
                max = max(penguins$flipper_length_mm),
                value = c(min(penguins$flipper_length_mm), max(penguins$flipper_length_mm))
                )
  )

)

#---------------------------------------------------------------------------#
# Serverkomponente
#---------------------------------------------------------------------------#

server <- function(input, output){

  # reaktive Objekt ausbauen

  #penguin_filter <- reactive(
  #  penguins %>%
  #    filter(body_mass_g >= input$weight[1] &
  #             body_mass_g <= input$weight[2])
  penguin_filter <- reactive(
    penguins %>%
      filter(flipper_length_mm >= input$length[1] &
               flipper_length_mm <= input$length[2])  
  )

  # Plot
  #output$Pinguinplot <- renderPlot(
  #  ggplot(data = penguin_filter(), aes(x = body_mass_g, y = flipper_length_mm))+
  #    geom_point()
  output$Pinguinplot <- renderPlot(
    ggplot(data = penguin_filter(), aes(x = species, y = flipper_length_mm))+
      geom_boxplot()
  )


}

#---------------------------------------------------------------------------#
# End of Program, Run Shiny
#---------------------------------------------------------------------------#

shinyApp(ui, server)
