package com.example.erikkoning.twitmine;


import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ProgressBar;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

import static android.widget.Toast.*;
import static com.example.erikkoning.twitmine.R.id.progressBar;
import static com.example.erikkoning.twitmine.R.id.responseView;


/**
 * A simple {@link Fragment} subclass.
 */
public class SearchFragment extends Fragment {

    //Global vars (NICE!)
    ProgressBar progressBar;
    TextView responseView;
    String str;
    String API_URL = "https://twitmine.herokuapp.com/sentimental/";


    public SearchFragment() {
        // Required empty public constructor
    }


    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View v = inflater.inflate(R.layout.fragment_search, container, false);
        Button button = (Button) v.findViewById(R.id.queryButton);
        progressBar = (ProgressBar) v.findViewById(R.id.progressBar);
        responseView = (TextView) v.findViewById(R.id.responseView);
        final EditText et = (EditText) v.findViewById(R.id.textInput);

        button.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View view) {

                str = et.getText().toString();
               
                new RetrieveFeedTask().execute();
            }
        });

        return v;
    }

    class RetrieveFeedTask extends AsyncTask<Void, Void, String> {

        private Exception exception;   //only this class has access (private)

        protected void onPreExecute() {
            progressBar.setVisibility(View.VISIBLE);
            Toast.makeText(getActivity(), "Executed", LENGTH_LONG).show();
            responseView.setText("");
        }

        protected String doInBackground(Void... urls) {
            // Do some validation here
            //
            try {
                URL url = new URL(API_URL + str);
                HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
                try {
                    BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(urlConnection.getInputStream()));
                    StringBuilder stringBuilder = new StringBuilder();
                    String line;
                    while ((line = bufferedReader.readLine()) != null) {
                        stringBuilder.append(line).append("\n");
                    }
                    bufferedReader.close();
                    return stringBuilder.toString();
                } finally {
                    urlConnection.disconnect();
                }
            } catch (Exception w) {
                Log.w("ERROR", w.getMessage(), w);
                return null;
            }
        }

        protected void onPostExecute(String response) {         //response is a Json string


            if (response == null) {
                response = "**LACK OF DATA**";
            }
            progressBar.setVisibility(View.GONE);
            Log.i("INFO", response);

            JSONObject myJson = null;
            try {
                myJson = new JSONObject(response);
            } catch (JSONException e) {
                e.printStackTrace();
            }

            String result = myJson.optString("result");

            //String status = myJson.optString("status");


            responseView.setText(result);                //responseView is name of textbox, .setText is function

        }


    }
}
