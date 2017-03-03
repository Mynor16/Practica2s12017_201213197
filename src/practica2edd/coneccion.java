/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package practica2edd;


import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;
import java.io.IOException;

import java.net.MalformedURLException;
import java.net.URL;

/**
 *
 * @author Mynor
 */
public class coneccion {
    
    public static OkHttpClient webClient = new OkHttpClient();
    
    
    public static String insertLista(String palabra){
        
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato",palabra)
                .build();
        try {
            URL url = new URL("http://0.0.0.0:5000/insertarLista");
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
       return null;
    }
    public static String deleteLista(String id){
        
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato",id+"")
                .build();
        try {
            URL url = new URL("http://0.0.0.0:5000/eliminarLista");
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
       return null;
    }
    
    public static String serchLista(String busqueda){
        
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato",busqueda)
                .build();
        try {
            URL url = new URL("http://0.0.0.0:5000/buscaLista");
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
       return null;
    }
}
