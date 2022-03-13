//    \  |  |       _ \    \ __ __|  \       __|  __| __ __| __ __| __|  _ \ 
//   |\/ |  |       |  |  _ \   |   _ \     (_ |  _|     |      |   _|     / 
//  _|  _| ____|   ___/ _/  _\ _| _/  _\   \___| ___|   _|     _|  ___| _|_\

int x = 1 ; 

int bars;

int bars_last;

float table[34];

float OpenPrice;

void OnStart(){
  
  if(x==1||Close[1]>High[1]){
  
   x=0;
   
   bars=Bars;
   
   OpenPrice=Close[1];
   
   ChartScreenShot(0,IntegerToString(Bars)+,1280,800,ALIGN_RIGHT);
   
   low = Low[1]-2*(Ask-Bid); // Stop
   
   if(new_bar&&Bars-bars<30){
   
   table[Bars-bars]=Close[1]-OpenPrice;
   
   };
   
   if(Bars-bars>30||Ask<low){
   
   save_csv(ArrayMaximum(table));
   
   };
   
   };

};

int save_csv(string name){

   int file_handle = FileOpen("Csv_data.csv",FILE_READ|FILE_WRITE|FILE_CSV);

   FileWrite(file_handle,IntegerToString(Bars),IntegerToString(name));
   
   FileClose(file_handle);
     
   };
   
int new_bars(){
   
   if(Bars==bars_last+1){
   
   return(True);
   
   bars_last=Bars;
   
   };
   
};
   
   
   
   
   
   
  
   
         
            
         
         
         
         
            

            
      
      
      
      

   

   