
package com.miapp;

import android.app.Activity;
import android.widget.TextView;
import android.os.Bundle;

public class miapp extends Activity
{
    /** Se llama cuando la actividad se crea por primera vez. */
    @Override
    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);

        /* Cree un objeto TextView y establezca el texto en "Hola a todos". */
        TextView  tv = new TextView(this);
        tv.setText("Hello World!");
        setContentView(tv);
    }
}
